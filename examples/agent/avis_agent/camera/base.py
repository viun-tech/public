from abc import ABC, abstractmethod
from pathlib import Path
from typing import Union

from avis_agent.core.exceptions import AgentError
from avis_agent.utils import BaseSettingsWithRetries
from PIL.Image import Image


class BaseCameraSettings(BaseSettingsWithRetries):
    name: str
    image_path: Path


class AbstractCamera(ABC):
    def __init__(self, config: BaseCameraSettings) -> None:
        self.config = config

    @abstractmethod
    def start(self) -> Union[bool, AgentError]:
        """Start the camera.

        Returns:
            is_started_or_error (bool | AgentError): Whether the camera is ready or not or an AgentError.
        """
        ...

    @abstractmethod
    def check_camera_ready(self) -> bool:
        """Check if the camera is ready.

        Returns:
            is_ready (bool): Whether the camera is ready or not.
        """
        ...

    @abstractmethod
    def capture_image(self) -> Union[Image, AgentError]:
        """Capture an image.

        Returns:
            image (Image | AgentError): The captured image or an AgentError.
        """
        ...

    @abstractmethod
    def stop(self) -> Union[bool, AgentError]:
        """Stop the camera.

        Returns:
            is_stopped_or_error (bool | AgentError): Whether the camera is stopped or not or an AgentError.
        """
        ...

    @classmethod
    def build(cls, config: BaseCameraSettings):
        if config.name == "oak_d_poe":
            from avis_agent.camera.impl.oak_d_poe import OakDPOECamera

            return OakDPOECamera(config)
        elif config.name == "mock":
            from avis_agent.camera.impl.mock import MockCamera

            return MockCamera(config)
        else:
            raise ValueError(f"Unknown camera name: {config.name}")
