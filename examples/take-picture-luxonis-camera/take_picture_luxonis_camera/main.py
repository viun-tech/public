import logging
from enum import Enum
from typing import Union

import cv2
import depthai as dai
import PIL.Image as img
from PIL.Image import Image
from pydantic import BaseModel
from pydantic_settings import BaseSettings

logger = logging.getLogger(__name__)


class CropCoordinates(BaseModel):
    """
    left: Left X coordinate of rectangle
    upper: Upper Y coordinate of rectangle
    right: Right X coordinate of rectangle
    lower: Lower Y coordinate of rectangle
    """

    left: float
    upper: float
    right: float
    lower: float


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


class CameraSettings(BaseSettings):
    resolution: CameraResolution = CameraResolution.the_1080_p
    crop: Union[CropCoordinates, None] = None
    fixed_focus: Union[int, None] = None
    device_info: Union[str, None] = None


class OakDPOECamera:
    def __init__(self, config: CameraSettings) -> None:
        self.pipeline = None
        self.device: Union[dai.Device, None] = None
        self.queue: Union[dai.DataOutputQueue, None] = None
        self.camera_started = False
        self.config = config

    def setup_camera(self) -> dai.Pipeline:
        pipeline = dai.Pipeline()

        cam_rgb = pipeline.create(dai.node.ColorCamera)
        cam_rgb.setBoardSocket(dai.CameraBoardSocket.RGB)
        cam_rgb.setResolution(self.config.resolution.dai_resolution)
        if self.config.fixed_focus is not None:
            cam_rgb.initialControl.setManualFocus(self.config.fixed_focus)
        else:
            cam_rgb.initialControl.setAutoFocusMode(
                dai.RawCameraControl.AutoFocusMode.CONTINUOUS_VIDEO
            )

        cam_rgb.setInterleaved(False)

        xout_rgb = pipeline.create(dai.node.XLinkOut)
        xout_rgb.setStreamName("rgb")
        cam_rgb.video.link(xout_rgb.input)

        return pipeline

    def start(self) -> bool:
        self.pipeline = self.setup_camera()
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
            raise Exception(f"Exception when starting camera: {e}")

    def check_camera_ready(self) -> bool:
        return self.camera_started

    def capture_image(self) -> Image:
        if not self._camera_started():
            raise Exception("Camera not started. Call start_camera first.")
        try:
            frame = self.queue.get()  # type: ignore
            # Convert the frame data to an image (using OpenCV and then PIL)
            img_np = frame.getCvFrame()
            img_pil = img.fromarray(cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB))
            if self.config.crop is not None:
                img_pil = img_pil.crop(
                    (
                        self.config.crop.left,
                        self.config.crop.upper,
                        self.config.crop.right,
                        self.config.crop.lower,
                    )
                )
            return img_pil
        except Exception as e:
            # If there is an exception, try to restart the camera
            self.stop()
            self.start()
            raise Exception(f"Exception when capturing image: {e}")

    def _camera_started(self) -> bool:
        return (
            self.camera_started and self.device is not None and self.queue is not None
        )

    def stop(self) -> bool:
        if not self._camera_started():
            raise Exception("Camera not started. Call start first.")
        try:
            self.device.close()  # type: ignore
            self.camera_started = False
            return True
        except Exception as e:
            raise Exception(f"Exception when stopping camera: {e}")


if __name__ == "__main__":
    config = CameraSettings(
        crop=CropCoordinates(xmin=0, ymin=0, xmax=1, ymax=1),
        resolution=CameraResolution.the_1080_p,
        fixed_focus=0,
        device_info="localhost:3456",
    )
    camera = OakDPOECamera(config)
    camera.start()
    image = camera.capture_image()
    image.show()
    camera.stop()
