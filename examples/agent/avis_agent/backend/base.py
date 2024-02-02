import io
from abc import ABC, abstractmethod
from typing import Union

from PIL import Image

from avis_agent.core.commands import (
    AbstractCommand,
    AddImageCommand,
    GetCaseInspectionResultCommand,
    ReadyCommand,
    StartCaseCommand,
)
from avis_agent.core.exceptions import AgentError
from avis_agent.core.responses import AbstractResponse, ReadyResponse
from avis_agent.utils import BaseSettingsWithRetries


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
        if type(command) is StartCaseCommand:
            return self.start_case()
        elif type(command) is AddImageCommand:
            if command.case_id is None or command.image is None:
                raise ValueError(
                    "AddImageCommand requires a case_id and an image to be set"
                )
            return self.add_image_to_case(command.case_id, str(command.image))
        elif type(command) is GetCaseInspectionResultCommand:
            if command.case_id is None:
                raise ValueError("GetCaseInspectionResultCommand requires a case_id")
            return self.get_case_inspection_result(command.case_id)
        else:
            raise NotImplementedError

    """Class for communicating with the backend of AVIS and execute the required chain of operations to perform a task."""

    @abstractmethod
    def start_case(self) -> Union[AbstractResponse, AgentError]:
        """
        Open a new case.

        Returns: should return either a CommandSuccessfulResponse or a CommandFailedResponse or an AgentError
        """
        ...

    @abstractmethod
    def get_case_inspection_result(
        self, case_id: int
    ) -> Union[AbstractResponse, AgentError]:
        """
        Get the inspection result of a case.
        Args:
            case_id: The ID of the case to get the inspection result of.

        Returns: should return either a QualityTestSuccessfulResponse, a QualityTestFailedResponse, a QualityTestUncertainResponse or an AgentError
        """
        ...

    @abstractmethod
    def add_image_to_case(
        self, case_id: int, image: str
    ) -> Union[AbstractResponse, AgentError]:
        """
        Add an image to a case.

        Args:
            case_id: The ID of the case to add the image to.
            image: The path to the image to add to the case.

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
