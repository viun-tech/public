import io
from abc import ABC, abstractmethod
from typing import Union

from avis_agent.core.commands import (
    AbstractCommand,
    AddImageCommand,
    GetInspectionResultCommand,
    ReadyCommand,
    StartInspectionCommand,
)
from avis_agent.core.exceptions import AgentError
from avis_agent.core.responses import AbstractResponse, ReadyResponse
from avis_agent.utils import BaseSettingsWithRetries
from PIL import Image


def image_to_byte_array(image: Image) -> bytes:
    byte_array = io.BytesIO()
    image.save(byte_array, format=image.format)
    return byte_array.getvalue()


class BaseBackendSettings(BaseSettingsWithRetries):
    name: str


class AbstractBackend(ABC):
    def __init__(self, config: BaseBackendSettings) -> None:
        self.config = config

    def execute(self, command: AbstractCommand) -> Union[AbstractResponse, AgentError]:
        """
        Execute a command.

        Args:
            command: The command to execute.

        Returns: should return either a CommandSuccessfulResponse, a CommandFailedResponse, a QualityTestSuccessfulResponse, a QualityTestFailedResponse, a QualityTestUncertainResponse or an AgentError

        """
        if type(command) is ReadyCommand:
            return ReadyResponse()
        if type(command) is StartInspectionCommand:
            return self.start_inspection()
        elif type(command) is AddImageCommand:
            if command.inspection_id is None or command.image is None:
                raise ValueError(
                    "AddImageCommand requires a inspection_id and an image to be set"
                )
            return self.add_image_to_inspection(
                command.inspection_id, str(command.image)
            )
        elif type(command) is GetInspectionResultCommand:
            if command.inspection_id is None:
                raise ValueError("GetInspectionResultCommand requires a inspection_id")
            return self.get_inspection_result(command.inspection_id)
        else:
            raise NotImplementedError

    """Class for communicating with the backend of AVIS and execute the required chain of operations to perform a task."""

    @abstractmethod
    def start_inspection(self) -> Union[AbstractResponse, AgentError]:
        """
        Open a new inspection.

        Returns: should return either a CommandSuccessfulResponse or a CommandFailedResponse or an AgentError
        """
        ...

    @abstractmethod
    def get_inspection_result(
        self, inspection_id: int
    ) -> Union[AbstractResponse, AgentError]:
        """
        Get the inspection result of a inspection.
        Args:
            inspection_id: The ID of the inspection to get the inspection result of.

        Returns: should return either a QualityTestSuccessfulResponse, a QualityTestFailedResponse, a QualityTestUncertainResponse or an AgentError
        """
        ...

    @abstractmethod
    def add_image_to_inspection(
        self, inspection_id: int, image: str
    ) -> Union[AbstractResponse, AgentError]:
        """
        Add an image to a inspection.

        Args:
            inspection_id: The ID of the inspection to add the image to.
            image: The path to the image to add to the inspection.

        Returns: should return either a CommandSuccessfulResponse, a CommandFailedResponse or an AgentError

        """
        ...

    @classmethod
    def build(cls, config: BaseBackendSettings):
        if config.name == "avis":
            from avis_agent.backend.impl.avis import AvisBackend

            return AvisBackend(config)
        else:
            raise ValueError(f"Unknown backend name: {config.name}")
