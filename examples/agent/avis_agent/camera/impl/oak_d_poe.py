import logging
from enum import Enum
from typing import Annotated, Literal, Union

import cv2
import depthai as dai
import PIL.Image as img
from avis_agent.camera.base import AbstractCamera, BaseCameraSettings
from avis_agent.core.exceptions import AgentError
from PIL.Image import Image
from pydantic import BaseModel, Field, confloat

logger = logging.getLogger(__name__)

Ratio = Annotated[float, confloat(ge=0, le=1), Field(...)]


class CropCoordinates(BaseModel):
    """
    xmin: Top left X coordinate of rectangle normalized between 0 and 1
    ymin: Top left Y coordinate of rectangle normalized between 0 and 1
    xmax: Bottom right X coordinate of rectangle normalized between 0 and 1
    ymax: Bottom right Y coordinate of rectangle normalized between 0 and 1
    """

    xmin: Ratio
    ymin: Ratio
    xmax: Ratio
    ymax: Ratio


class CameraResolution(str, Enum):
    the_1080_p = "1080p"
    the_4_k = "4k"

    @property
    def dai_resolution(self):
        if self == CameraResolution.the_1080_p:
            return dai.ColorCameraProperties.SensorResolution.THE_1080_P
        elif self == CameraResolution.the_4_k:
            return dai.ColorCameraProperties.SensorResolution.THE_4_K
        else:
            raise NotImplementedError


class OakDPOECameraSettings(BaseCameraSettings):
    name: Literal["oak_d_poe"]
    resolution: CameraResolution = CameraResolution.the_1080_p
    fixed_focus: Union[int, None] = None
    crop: Union[CropCoordinates, None] = None
    device_info: Union[str, None] = None


class OakDPOECamera(AbstractCamera):
    def __init__(self, config: OakDPOECameraSettings) -> None:
        super().__init__(config)
        self.pipeline = None
        self.device: Union[dai.Device, None] = None
        self.queue: Union[dai.DataOutputQueue, None] = None
        self.camera_started = False

    def is_crop_valid(self) -> bool:
        """Test if the cropping coordinates are valid. The coordinates are valid if the width is divisible by 2 and the height by 3.

        Returns:
            is_valid (bool): Whether the cropping coordinates are valid or not.
        """
        return (self.config.crop.xmax - self.config.crop.xmin) % 2 == 0 and (
            self.config.crop.ymax - self.config.crop.ymin
        ) % 3 == 0

    def setup_camera(self) -> dai.Pipeline:
        pipeline = dai.Pipeline()

        if self.config.crop is not None and not self.is_crop_valid():
            raise AgentError(
                f"The cropping coordinates are invalid. The width ({self.config.crop.xmax - self.config.crop.xmin}) must be divisible by 2 and the height ({self.config.crop.ymax - self.config.crop.ymin}) by 3."
            )

        cam_rgb = pipeline.create(dai.node.ColorCamera)
        cam_rgb.setBoardSocket(dai.CameraBoardSocket.RGB)
        cam_rgb.setResolution(self.config.resolution.dai_resolution)
        if self.config.fixed_focus is not None:
            cam_rgb.initialControl.setManualFocus(self.config.fixed_focus)
        else:
            cam_rgb.initialControl.setAutoFocusMode(
                dai.RawCameraControl.AutoFocusMode.CONTINUOUS_VIDEO
            )

        if self.config.crop is not None:
            # Set the dimensions of the captured area
            video_width = int(
                (self.config.crop.xmax - self.config.crop.xmin) * cam_rgb.getIspWidth()
            )
            video_height = int(
                (self.config.crop.ymax - self.config.crop.ymin) * cam_rgb.getIspHeight()
            )
            cam_rgb.setVideoSize(video_width, video_height)

            # Set the cropping position of the capture area
            cam_rgb.setSensorCrop(x=self.config.crop.xmin, y=self.config.crop.ymin)

        cam_rgb.setInterleaved(False)

        xout_rgb = pipeline.create(dai.node.XLinkOut)
        xout_rgb.setStreamName("rgb")
        cam_rgb.video.link(xout_rgb.input)

        return pipeline

    def start(self) -> Union[bool, AgentError]:
        self.pipeline = self.config.with_retries(self.setup_camera)
        try:
            if self.config.device_info is not None:
                self.device = dai.Device(
                    self.pipeline, dai.DeviceInfo(self.config.device_info)
                )
            else:
                self.device = dai.Device(self.pipeline)
            self.camera_started = True
            self.queue = self.device.getOutputQueue(  # type: ignore
                name="rgb", maxSize=1, blocking=False
            )
            return True
        except Exception as e:
            self.camera_started = False
            return AgentError(f"Exception when starting camera: {e}")

    def check_camera_ready(self) -> bool:
        return self.camera_started

    def capture_image(self) -> Union[Image, AgentError]:
        if not self._camera_started():
            return AgentError("Camera not started. Call start_camera first.")
        try:
            frame = self.queue.get()  # type: ignore
            # Convert the frame data to an image (using OpenCV and then PIL)
            img_np = frame.getCvFrame()
            img_pil = img.fromarray(cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB))
            return img_pil
        except Exception as e:
            # If there is an exception, try to restart the camera
            self.stop()
            self.start()
            return AgentError(f"Exception when capturing image: {e}")

    def _camera_started(self) -> bool:
        return (
            self.camera_started and self.device is not None and self.queue is not None
        )

    def stop(self) -> Union[bool, AgentError]:
        if not self._camera_started():
            return AgentError("Camera not started. Call start first.")
        try:
            self.device.close()  # type: ignore
            self.camera_started = False
            return True
        except Exception as e:
            return AgentError(f"Exception when stopping camera: {e}")
