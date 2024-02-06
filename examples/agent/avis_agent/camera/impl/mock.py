from typing import Literal, Union

import numpy as np
from PIL import Image as img
from PIL.Image import Image

from avis_agent.camera.base import AbstractCamera, BaseCameraSettings
from avis_agent.core.exceptions import AgentError


class MockCameraSettings(BaseCameraSettings):
    name: Literal["mock"]


class MockCamera(AbstractCamera):
    """Mock camera for testing purposes.

    This camera is used to test the agent without having to connect to the real camera.
    """

    def start(self) -> Union[bool, AgentError]:
        return True

    def __init__(
        self,
        config: MockCameraSettings,
    ):
        super().__init__(config)
        self.is_ready = True
        self.random_image_shape = (10, 10, 3)

    def check_camera_ready(self) -> bool:
        return self.is_ready

    def capture_image(self) -> Image:
        image = img.fromarray(
            np.random.randint(0, 255, size=self.random_image_shape, dtype=np.uint8)
        )
        image.save(self.config.image_path)
        return image

    def stop(self) -> Union[bool, AgentError]:
        return True
