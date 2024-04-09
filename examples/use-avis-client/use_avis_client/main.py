import datetime
import logging
from typing import List

import pytz
from avis_client import (
    ApiClient,
    InspectionApi,
    Configuration,
    ImageApi,
    ImageAttributeApi,
    ResultApi,
)
from avis_client.models.inspection_request import InspectionRequest
from avis_client.models.patched_inspection_request import PatchedInspectionRequest
from avis_client.rest import ApiException

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

avis_uri = "https://avis.vu.engineering"
api_key = "<your api key>"

config = Configuration(
    host=avis_uri,
    api_key={"ApiKeyAuth": api_key},
)

def create_inspection(
    team_id: int, configuration_id: int, api_config: Configuration = config
) -> int:
    with ApiClient(api_config) as api_client:
        api_instance = InspectionApi(api_client)
        inspection_request = InspectionRequest(
            team=team_id,
            configuration=configuration_id,
        )
        try:
            api_response = api_instance.inspection_create(
                inspection_request=inspection_request,
            )
            return api_response.id
        except ApiException as e:
            msg = f"Api exception when calling InspectionApi->inspection_create:  {e}\n"
            logger.error(msg)
            raise Exception(msg)


def close_inspection(
    inspection_id: int, membership_id: int, api_config: Configuration = config
) -> bool:
    with ApiClient(api_config) as api_client:
        api_instance = InspectionApi(api_client)
        inspection_request = PatchedInspectionRequest(
            closed_by=membership_id,
            close_datetime=datetime.datetime.now(tz=pytz.utc),
        )
        try:
            api_response = api_instance.inspection_partial_update(
                id=inspection_id,
                patched_inspection_request=inspection_request,
            )
            if api_response.id == inspection_id:
                logger.info(f"Inspection {inspection_id} closed successfully")
                return True
            else:
                logger.error(f"Inspection {inspection_id} not closed")
                return False
        except ApiException as e:
            msg = f"Api exception when calling InspectionApi->inspection_partial_update:  {e}\n"
            logger.error(msg)
            raise Exception(msg)


def add_image_to_inspection(
    team_id: int, inspection_id: int, image: str, api_config: Configuration = config
) -> int:
    with ApiClient(api_config) as api_client:
        api_instance = ImageApi(api_client)
        image_request = {
            "file": image,
            "team": team_id,
            "inspection": inspection_id,
            "capture_datetime": datetime.datetime.now(tz=pytz.utc),
        }
        try:
            api_response = api_instance.image_create(**image_request)
            logger.info(f"Image added to inspection {inspection_id} successfully")
            return api_response.id
        except ApiException as e:
            msg = f"Exception when calling ImageApi->image_create:  {e}\n"
            logger.error(msg)
            raise Exception(msg)

def get_image_attributes(
    image_id: int, api_config: Configuration = config
) -> List[str]:
    with ApiClient(api_config) as api_client:
        image_client = ImageApi(api_client)
        image_attribute_client = ImageAttributeApi(api_client)
        result_client = ResultApi(api_client)
        try:
            image_response = image_client.image_retrieve(id=image_id)
            if image_response.results is None or len(image_response.results) == 0:
                logger.info(f"Image {image_id} has no results")
                return []
            result_list = result_client.result_list(id=image_response.results)
            attributes = [
                image_attribute
                for result in result_list
                for image_attribute in result.image_attributes
            ]
            if len(attributes) == 0:
                logger.info(f"Image {image_id} has no attributes")
                return []
            image_attribute_list = image_attribute_client.image_attribute_list(
                id=attributes
            )
            return [attribute.value for attribute in image_attribute_list.results]
        except ApiException as e:
            msg = f"Exception when retrieving image attributes:  {e}\n"
            logger.error(msg)
            raise Exception(msg)


if __name__ == "__main__":
    # <replace with your team id>
    team_id = 1
    # <replace with your configuration id>
    configuration_id = 1
    # open inspection
    inspection_id = create_inspection(team_id, configuration_id=configuration_id)
    logger.info(f"Inspection {inspection_id} created")
    # <replace with a local path to a picture>
    image = "path/to/image.jpg"
    # add image to inspection
    image_id = add_image_to_inspection(team_id, inspection_id, image)
    logger.info(f"Image {image_id} added to inspection {inspection_id}")
    # get image attributes
    image_attributes = get_image_attributes(image_id)
    logger.info(f"Image attributes: {image_attributes}")
    # continue cycle if needed or
    # close inspection
