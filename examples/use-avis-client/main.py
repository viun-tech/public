import datetime
import logging

import pytz
from avis_client import ApiClient, InspectionApi, Configuration, ImageApi
from avis_client.models.inspection_request import InspectionRequest
from avis_client.rest import ApiException

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

avis_uri = "https://avis.vu.engineering"
api_key = "your api key"

openapi_client_config = Configuration(
    host=avis_uri,
    api_key={"ApiKeyAuth": api_key},
)


def create_inspection(team_id: int, inspection_object_id: int) -> int:
    with ApiClient(openapi_client_config) as api_client:
        api_instance = InspectionApi(api_client)
        inspection_request = InspectionRequest(
            team=team_id,
            inspection_object=inspection_object_id,
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


def get_inspection_status(inspection_id: int) -> str:
    with ApiClient(openapi_client_config) as api_client:
        api_instance = InspectionApi(api_client)
        try:
            api_response = api_instance.inspection_status_list(id=[inspection_id])
            status = next(
                filter(lambda x: x.id == inspection_id, api_response)
            ).inspection_status
            return status
        except ApiException as e:
            msg = f"Exception when calling InspectionApi->inspection_inspection_status_list:  {e}\n"
            logger.error(msg)
            raise Exception(msg)
        except StopIteration:
            msg = f"Inspection status for inspection {inspection_id} not found\n"
            logger.error(msg)
            raise Exception(msg)


def add_image_to_inspection(team_id: int, inspection_id: int, image: str) -> int:
    with ApiClient(openapi_client_config) as api_client:
        api_instance = ImageApi(api_client)
        params = {
            "file": image,
            "team": team_id,
            "inspection": inspection_id,
            "capture_datetime": datetime.datetime.now(tz=pytz.utc),
        }
        try:
            api_response = api_instance.image_create(**params)
            logger.info(f"Image added to inspection {inspection_id} successfully")
            return api_response.id
        except ApiException as e:
            msg = f"Exception when calling ImageApi->image_create:  {e}\n"
            logger.error(msg)
            raise Exception(msg)


if __name__ == "__main__":
    team_id = 1
    inspection_object_id = 1
    inspection_id = create_inspection(team_id, inspection_object_id)
    logger.info(f"Inspection {inspection_id} created")
    image = "path/to/image.jpg"
    image_id = add_image_to_inspection(team_id, inspection_id, image)
    logger.info(f"Image {image_id} added to inspection {inspection_id}")
    status = get_inspection_status(inspection_id)
    logger.info(f"Status for inspection {inspection_id}: {status}")
