import logging
import time
from typing import Type, Union

from avis_agent.backend.base import AbstractBackend
from avis_agent.backend.impl.avis import AvisBackendSettings
from avis_agent.camera.base import AbstractCamera
from avis_agent.camera.impl.mock import MockCameraSettings
from avis_agent.camera.impl.oak_d_poe import OakDPOECameraSettings
from avis_agent.core.commands import (
    AbstractCommand,
    AddImageCommand,
    ReadyCommand,
    StartInspectionCommand,
    StatefulCommandTypes,
)
from avis_agent.core.exceptions import AgentError
from avis_agent.core.responses import (
    AbstractResponse,
    CommandFailedResponse,
    CommandSuccessfulResponse,
    ReadyResponse,
)
from avis_agent.signal.base import AbstractSignal
from avis_agent.signal.impl.cli import CliSignalSettings
from avis_agent.signal.impl.modbus_tcp import ModbusTcpSignalSettings
from avis_agent.utils import BaseSettingsWithRetries
from PIL.Image import Image
from pydantic import Field
from pydantic_settings import SettingsConfigDict

logger = logging.getLogger(__name__)

CameraSettings = Union[MockCameraSettings, OakDPOECameraSettings]
BackendSettings = Union[AvisBackendSettings]
SignalSettings = Union[CliSignalSettings, ModbusTcpSignalSettings]


class AgentSettings(BaseSettingsWithRetries):
    camera: CameraSettings = Field(..., discriminator="name")
    backend: BackendSettings = Field(..., discriminator="name")
    signal: SignalSettings = Field(..., discriminator="name")

    model_config = SettingsConfigDict(env_prefix="AGENT_", env_nested_delimiter="__")


class Agent:
    def __init__(
        self,
        backend: AbstractBackend,
        camera: AbstractCamera,
        signal: AbstractSignal,
        config: AgentSettings,
    ) -> None:
        """
        Initialize the Agent with the necessary dependencies.
        Args:
            backend: The backend system to persist data.
            camera: The camera system to capture images.
            signal: The signal interface to read/write commands and responses.
            config: Configuration settings for the agent and its dependencies.
        """
        self.backend, self.camera, self.signal, self.config = (
            backend,
            camera,
            signal,
            config,
        )
        self.last_command: Union[AbstractCommand, AgentError, None] = None
        self.last_response: Union[AbstractResponse, AgentError, None] = None
        self.current_inspection_id: Union[int, None] = None
        self.first_run = True
        self.current_image_sharpness = float(0)
        self.current_image_brightness = float(0)

    def run(self) -> None:
        """
        Run the agent.

        The agent will run in a loop, reading commands from the signal interface, executing them on the backend, and writing the response back to the signal interface.
        """
        try:
            if not self._start_camera():
                return
            while True:
                command = self.signal.read()
                # need acknowledgment from the other side before processing the next command
                if self._is_same_or_not_ready_command(command) or (
                    self._is_last_response_error_or_failed()
                    and not self._is_ready_command(command)
                ):
                    continue
                self.last_command = command
                self._process_command(command)
                self.first_run = False
                time.sleep(self.config.signal.polling_interval)
        finally:
            self.signal.close()
            self.camera.stop()

    def _is_last_response_error_or_failed(self) -> bool:
        """
        Check if the last response was an error or a failed response.
        """
        return isinstance(self.last_response, (AgentError, CommandFailedResponse))

    def _is_ready_command(self, command) -> bool:
        """
        Check if the command is a ReadyCommand.
        """
        return isinstance(command, ReadyCommand)

    def _is_same_or_not_ready_command(self, command) -> bool:
        """
        Check if the agent is ready to process the command. The agent cannot process a command if any of the following is true:
            * the current command is the same as the last command (to avoid processing the same command twice)
            * the previous command was not a ReadyCommand (i.e. the last command was not acknowledged)
        """
        return (
            isinstance(command, type(self.last_command))
            or not self._is_ready_command(self.last_command)
            and not self.first_run
            and not self._is_ready_command(command)
        )

    def _process_command(self, command) -> Union[AbstractResponse, AgentError]:
        response = self._handle_command(command)
        success = self._write_signal(response)
        if not success:
            msg = f"Failed to write response: {response}"
            logger.error(msg)
            response = CommandFailedResponse(message=msg)
        else:
            logger.info(f"Wrote response: {response}")
        if not isinstance(response, (AgentError, CommandFailedResponse)):
            self.current_inspection_id = self._get_inspection_id(command, response)
            self.last_command = command
        self.last_response = response
        return response

    def _write_signal(
        self, response: Union[AbstractResponse, AgentError]
    ) -> Union[bool, AgentError]:
        return self.signal.write(response)

    def _call_backend(
        self, command: AbstractCommand
    ) -> Union[AbstractResponse, AgentError]:
        return self.backend.execute(command)

    def _capture_image(self) -> Union[Image, AgentError]:
        image = self.camera.capture_image()
        if isinstance(image, AgentError):
            return image
        return image

    def _start_camera(self) -> bool:
        """
        Start the camera

        Returns:
            bool: True if the camera starts successfully, False otherwise.
        """
        camera_start_result = self.camera.start()

        if isinstance(camera_start_result, AgentError):
            logger.error(
                f"Got an error when starting the camera: {camera_start_result}"
            )
            self.signal.write(camera_start_result)
            return False
        return True

    def _handle_command(
        self, command: Union[AbstractCommand, AgentError]
    ) -> Union[AbstractResponse, AgentError]:
        """
        Handle the received command, execute it, and generate a response.


        Args:
            command: The command to be handled.

        Returns:
            Union[AbstractResponse, AgentError]: The result of the command execution or any error encountered.
        """
        # pre-process the command (e.g capture image)
        # if the command requires a inspection_id and the inspection_id is not set, we set it to the last inspection_id
        if isinstance(command, StatefulCommandTypes) and command.inspection_id is None:
            if self.current_inspection_id is None:
                return AgentError("The inspection ID is not known.")
            else:
                command.inspection_id = self.current_inspection_id

        logger.info(f"Received command: {command}")

        # if the command is AddImageCommand, we capture an image and set it to the command
        if isinstance(command, AddImageCommand):
            command = self._pre_process(command)

        if isinstance(command, AgentError):
            logger.error(f"Got an error when processing command: {command}")
            return command

        # execute the command on the backend
        response = self._call_backend(command)

        if isinstance(response, AgentError):
            logger.error(
                f"Got an error when calling the backend: {command} --> {response}"
            )
            return response

        return response

    def _pre_process(
        self, command: AddImageCommand
    ) -> Union[AddImageCommand, AgentError]:
        """
        Process the AddImageCommand, capturing an image, saving it to the local filesystem and attaching it to the command
        to be sent to the backend.

        Args:
            command: The AddImageCommand to be processed.

        Returns:
            Union[AddImageCommand, AgentError]: The processed command with the attached image or any error encountered.
        """
        if not self.camera.check_camera_ready():
            return AgentError("Camera is not ready")

        captured_image = self._capture_image()
        if isinstance(captured_image, AgentError):
            logger.error(f"Got an error when capturing image: {captured_image}")
            return captured_image

        captured_image.save(self.config.camera.image_path, format="PNG")
        command.image = self.config.camera.image_path
        return command

    def _get_inspection_id(
        self, command: Type[AbstractCommand], response: AbstractResponse
    ) -> Union[int, None]:
        """
        Determine the inspection ID based on the command and response.

        Args:
            command: The command received.
            response: The response generated after executing the command.

        Returns:
            Union[int, None]: The inspection ID or None.
        """
        if isinstance(command, ReadyCommand) or isinstance(response, ReadyResponse):
            return self.current_inspection_id
        if isinstance(command, StartInspectionCommand) and isinstance(
            response, CommandSuccessfulResponse
        ):
            return response.result
        if (
            isinstance(command, StatefulCommandTypes)
            and isinstance(self.last_command, ReadyCommand)
            and self.current_inspection_id is None
        ):
            raise RuntimeError("The inspection ID is not known.")
        return self.current_inspection_id
