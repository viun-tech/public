import datetime
import logging
from typing import Literal, Union

import pytz
from avis_agent.backend.base import AbstractBackend, BaseBackendSettings
from avis_agent.core.exceptions import AgentError
from avis_agent.core.responses import (
    CommandFailedResponse,
    CommandSuccessfulResponse,
    QualityTestFailedResponse,
    QualityTestSuccessfulResponse,
    QualityTestUncertainResponse,
)
from vue_avis_client import ApiClient, Configuration, ImageApi, InspectionApi
from vue_avis_client.models.image import Image
from vue_avis_client.models.inspection import Inspection
from vue_avis_client.models.inspection_request import InspectionRequest
from vue_avis_client.rest import ApiException

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class AvisBackendSettings(BaseBackendSettings):
    name: Literal["avis"]
    api_key: str
    team_id: int
    inspection_object_id: int
    uri: str


class AvisBackend(AbstractBackend):
    def __init__(self, config: AvisBackendSettings) -> None:
        super().__init__(config)
        self.team_id = config.team_id
        self.inspection_object_id = config.inspection_object_id
        self.openapi_client_config = Configuration(
            host=config.uri,
            api_key={"ApiKeyAuth": config.api_key},
        )

    def start_inspection(
        self,
    ) -> Union[CommandSuccessfulResponse, CommandFailedResponse, AgentError]:
        with ApiClient(self.openapi_client_config) as api_client:
            api_instance = InspectionApi(api_client)
            inspection_request = InspectionRequest(
                team=self.team_id,
                inspection_object=self.inspection_object_id,
            )
            try:
                api_response: Inspection = self.config.with_retries(
                    api_instance.inspection_create,
                    inspection_request=inspection_request,
                    _request_timeout=self.config.timeout,
                )
                msg = "Inspection created successfully"
                inspection_id = api_response.id
            except ApiException as e:
                msg = f"Api exception when calling InspectionApi->inspection_create:  {e}\n"
                logger.error(msg)
                return CommandFailedResponse(message=msg)
            except Exception as e:
                msg = (
                    f"Agent error when calling InspectionApi->inspection_create:  {e}\n"
                )
                logger.error(msg)
                return AgentError(msg)
            return CommandSuccessfulResponse(result=inspection_id, message=msg)

    def get_inspection_result(
        self, inspection_id: int
    ) -> Union[
        QualityTestSuccessfulResponse,
        QualityTestFailedResponse,
        QualityTestUncertainResponse,
        CommandFailedResponse,
        AgentError,
    ]:
        with ApiClient(self.openapi_client_config) as api_client:
            api_instance = InspectionApi(api_client)

            try:
                api_response = self.config.with_retries(
                    api_instance.inspection_status_list,
                    id=[inspection_id],
                    _request_timeout=self.config.timeout,
                )
                msg = "Inspection status retrieved successfully"
                status = next(
                    filter(lambda x: x.id == inspection_id, api_response)
                ).inspection_status
            except ApiException as e:
                msg = f"Exception when calling InspectionApi->inspection_status_list:  {e}\n"
                logger.error(msg)
                return CommandFailedResponse(message=msg)
            except StopIteration:
                msg = f"Inspection status for inspection {inspection_id} not found\n"
                status = None
            except Exception as e:
                msg = f"Agent error when calling InspectionApi->inspection_status_list:  {e}\n"
                logger.error(msg)
                return AgentError(msg)
            if status == "OK":
                return QualityTestSuccessfulResponse(result="OK", message=msg)
            elif status == "DEFECT":
                return QualityTestFailedResponse(result="DEFECT", message=msg)
            elif status == "NONE":
                return QualityTestUncertainResponse(result="NONE", message=msg)
            return CommandFailedResponse(message=msg)

    def add_image_to_inspection(
        self, inspection_id: int, image: str
    ) -> Union[CommandSuccessfulResponse, CommandFailedResponse, AgentError]:
        with ApiClient(self.openapi_client_config) as api_client:
            api_instance = ImageApi(api_client)
            params = {
                "file": image,
                "team": self.team_id,
                "inspection": inspection_id,
                "capture_datetime": datetime.datetime.now(tz=pytz.utc),
            }
            try:
                api_response: Image = self.config.with_retries(
                    api_instance.image_create, **params
                )
                msg = f"Image added to inspection {inspection_id} successfully"
                img_id = api_response.id
            except ApiException as e:
                msg = f"Exception when calling ImageApi->image_create:  {e}\n"
                logger.error(msg)
                return CommandFailedResponse(message=msg)
            except Exception as e:
                msg = f"Agent error when calling ImageApi->image_create:  {e}\n"
                logger.error(msg)
                return AgentError(msg)
            return CommandSuccessfulResponse(result=img_id, message=msg)
