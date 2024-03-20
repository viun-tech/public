import logging
import time
from typing import Callable, List

from take_picture_luxonis_camera.main import (
    OakDPOECamera,
    CameraSettings,
    CameraResolution,
    CropCoordinates,
)
from use_avis_client.main import (
    create_inspection,
    close_inspection,
    add_image_to_inspection,
    get_image_attributes,
)
from avis_client import Configuration

TEAM_ID = 1
CONFIGURATION_ID = 1
MEMBERSHIP_ID = 1
API_KEY = "1234"
API_URI = "https://avis.vu.engineering"
API_CONFIG = Configuration(host=API_URI, api_key={"ApiKeyAuth": API_KEY})
IMAGE_PATH = "image.png"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def wait_for_condition(
    func: Callable[[], bool], timeout: int = 8, raise_timeout: bool = False
) -> None:
    time_limit = time.time() + timeout
    while True:
        if time.time() > time_limit:
            if raise_timeout:
                raise Exception("Timeout waiting for result")
            else:
                break
        elif func():
            break
        time.sleep(0.5)


def capture_and_inspect_new_picture(
    team_id: int, inspection_id: int, image_path: str
) -> List[str]:
    image = camera.capture_image()
    image.save(image_path, format="PNG")
    logger.info(f"Image saved to {image_path}")
    image_id = add_image_to_inspection(team_id, inspection_id, image_path, API_CONFIG)
    logger.info(f"Image {image_id} added to inspection {inspection_id}")
    # wait for the image to be processed, should take at most a few seconds
    wait_for_condition(lambda: len(get_image_attributes(image_id, API_CONFIG)) > 0)
    return get_image_attributes(image_id, API_CONFIG)


def check_part(
    team_id: int,
    inspection_id: int,
    image_path: str,
    good_attributes: List[str],
    bad_attributes: List[str],
) -> bool:
    image_attributes = capture_and_inspect_new_picture(
        team_id, inspection_id, image_path
    )
    logger.info(f"Image attributes: {image_attributes}")
    if any(attribute in image_attributes for attribute in good_attributes):
        return True
    elif (
        any(attribute in image_attributes for attribute in bad_attributes)
        or len(image_attributes) == 0
    ):
        return False


if __name__ == "__main__":
    config = CameraSettings(
        device_info="192.168.1.80",
        resolution=CameraResolution.the_1080_p,
        fixed_focus=177,
        # crop rectangle with width 550 and height 400
        # that is located 819px from the left edge of the image and 240px from the top edge
        crop=CropCoordinates(left=819, upper=240, right=1369, lower=640),
    )
    camera = OakDPOECamera(config)
    camera.start()
    try:
        # wait for the camera to be ready
        wait_for_condition(camera.check_camera_ready, raise_timeout=True)
        while True:
            # open new inspection
            inspection_id = create_inspection(TEAM_ID, CONFIGURATION_ID, API_CONFIG)
            logger.info(f"Inspection {inspection_id} created")

            # grab blue base and inspect it, replace with actual code to wait for the part
            time.sleep(5)
            # inspect part
            while not check_part(
                team_id=TEAM_ID,
                inspection_id=inspection_id,
                image_path=IMAGE_PATH,
                good_attributes=["base_opening"],
                bad_attributes=["base_closure", "empty"],
            ):
                # drop part and grab a new one, replace with actual code to wait for the part
                time.sleep(5)

            # grab end-mill and inspect it, replace with actual code
            time.sleep(5)
            while not check_part(
                team_id=TEAM_ID,
                inspection_id=inspection_id,
                image_path=IMAGE_PATH,
                good_attributes=["top_opening"],
                bad_attributes=["top_closure", "empty"],
            ):
                # drop part and grab a new one, replace with actual code
                time.sleep(5)

            # cycle completed, close inspection
            close_inspection(inspection_id, MEMBERSHIP_ID, API_CONFIG)
    finally:
        camera.stop()
