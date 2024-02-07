import datetime
import logging

import pytz
from avis_client import ApiClient, CaseApi, Configuration, ImageApi
from avis_client.models.case_request import CaseRequest
from avis_client.rest import ApiException

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

avis_uri = "https://avis.vu.engineering"
api_key = "your api key"

openapi_client_config = Configuration(
    host=avis_uri,
    api_key={"ApiKeyAuth": api_key},
)


def create_case(team_id: int, inspection_object_id: int) -> int:
    with ApiClient(openapi_client_config) as api_client:
        api_instance = CaseApi(api_client)
        case_request = CaseRequest(
            team=team_id,
            inspection_object=inspection_object_id,
        )
        try:
            api_response = api_instance.case_create(
                case_request=case_request,
            )
            return api_response.id
        except ApiException as e:
            msg = f"Api exception when calling CaseApi->case_create:  {e}\n"
            logger.error(msg)
            raise Exception(msg)


def get_case_inspection_result(case_id: int) -> str:
    with ApiClient(openapi_client_config) as api_client:
        api_instance = CaseApi(api_client)
        try:
            api_response = api_instance.case_inspection_status_list(id=[case_id])
            status = next(
                filter(lambda x: x.id == case_id, api_response)
            ).inspection_status
            return status
        except ApiException as e:
            msg = f"Exception when calling CaseApi->case_inspection_status_list:  {e}\n"
            logger.error(msg)
            raise Exception(msg)
        except StopIteration:
            msg = f"Inspection status for case {case_id} not found\n"
            logger.error(msg)
            raise Exception(msg)


def add_image_to_case(team_id: int, case_id: int, image: str) -> int:
    with ApiClient(openapi_client_config) as api_client:
        api_instance = ImageApi(api_client)
        params = {
            "file": image,
            "team": team_id,
            "case": case_id,
            "capture_datetime": datetime.datetime.now(tz=pytz.utc),
        }
        try:
            api_response = api_instance.image_create(**params)
            logger.info(f"Image added to case {case_id} successfully")
            return api_response.id
        except ApiException as e:
            msg = f"Exception when calling ImageApi->image_create:  {e}\n"
            logger.error(msg)
            raise Exception(msg)


if __name__ == "__main__":
    team_id = 1
    inspection_object_id = 1
    case_id = create_case(team_id, inspection_object_id)
    logger.info(f"Case {case_id} created")
    image = "path/to/image.jpg"
    image_id = add_image_to_case(team_id, case_id, image)
    logger.info(f"Image {image_id} added to case {case_id}")
    status = get_case_inspection_result(case_id)
    logger.info(f"Inspection status for case {case_id}: {status}")
