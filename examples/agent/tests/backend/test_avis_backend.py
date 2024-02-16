import tempfile
from unittest.mock import MagicMock

import pytest
from avis.apps.core.models import Image, Inspection
from avis.apps.teams.models import Team
from avis.apps.users.models import CustomUser
from avis.tests.factories import (
    make_image,
    make_inspection,
    make_product,
    make_rating_inspection_result,
)
from avis_agent.backend.impl.avis import AvisBackend, AvisBackendSettings
from avis_agent.core.exceptions import AgentError
from avis_agent.core.responses import CommandFailedResponse
from django.core.files.images import ImageFile
from pytest_django.live_server_helper import LiveServer
from vue_avis_client import ApiException, ImageApi, InspectionApi

pytestmark = pytest.mark.django_db


# use local storage for images instead of Azure blob storage
@pytest.fixture(autouse=True)
def store_images_locally(use_filesystem_storage):
    pass


@pytest.fixture
def image_file(test_image) -> str:
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".gif")
    img_data = test_image.file.read()
    temp_file.write(img_data)
    temp_file.close()
    return temp_file.name


@pytest.fixture
def vue_avis_client(
    api_key: str, user: CustomUser, test_team: Team, live_server: LiveServer
) -> AvisBackend:
    inspection_object = make_product(team=test_team, save=True)
    config = AvisBackendSettings(
        name="avis",
        api_key=api_key,
        team_id=test_team.id,
        inspection_object_id=inspection_object.id,
        uri=live_server.url,
    )
    return AvisBackend(config)


def test_start_inspection(vue_avis_client: AvisBackend) -> None:
    response = vue_avis_client.start_inspection()
    assert not isinstance(response, AgentError)
    inspections = Inspection.objects.all()
    assert len(inspections) == 1
    assert inspections[0].id == response.result
    assert response.message == "Inspection created successfully"


def test_get_inspection_result(
    vue_avis_client: AvisBackend,
    test_team: Team,
    user: CustomUser,
    test_image: ImageFile,
) -> None:
    inspection_result = make_rating_inspection_result(
        team=test_team, user=user, save=True
    )
    inspection_result.rating = 1
    inspection_result.save()
    image = make_image(
        team=test_team,
        user=user,
        file=test_image,
        inspection_results=[inspection_result],
        save=True,
    )
    inspection = make_inspection(team=test_team, user=user, images=[image], save=True)
    response = vue_avis_client.get_inspection_result(inspection.id)
    assert not isinstance(response, AgentError)
    assert response.result == "DEFECT"
    assert response.message == "Inspection status retrieved successfully"

    inspection_result.rating = 5
    inspection_result.save()

    response = vue_avis_client.get_inspection_result(inspection.id)
    assert not isinstance(response, AgentError)
    assert response.result == "OK"
    assert response.message == "Inspection status retrieved successfully"


def test_add_image_to_inspection(
    vue_avis_client: AvisBackend,
    test_team: Team,
    user: CustomUser,
    image_file: str,
) -> None:
    inspection = make_inspection(team=test_team, user=user, images=[], save=True)
    assert inspection.images.count() == 0

    with open(image_file, "rb") as f:
        img_data = f.read()

    # add the image to the inspection
    response = vue_avis_client.add_image_to_inspection(inspection.id, image_file)
    assert not isinstance(response, AgentError)

    db_image = Image.objects.all()
    assert len(db_image) == 1
    assert db_image[0].id == response.result
    assert response.message == f"Image added to inspection {inspection.id} successfully"
    inspection.refresh_from_db()
    assert inspection.images.count() == 1
    assert inspection.images.first().file.read() == img_data


def test_retries_api_failure_start_inspection(monkeypatch, vue_avis_client):
    api_mock = MagicMock(side_effect=ApiException(reason="API failure", status=500))
    monkeypatch.setattr(InspectionApi, "inspection_create", api_mock)

    assert isinstance(vue_avis_client.start_inspection(), CommandFailedResponse)

    assert 3 == api_mock.call_count


def test_retries_api_failure_inspection_result(monkeypatch, vue_avis_client):
    api_mock = MagicMock(side_effect=ApiException(reason="API failure", status=500))
    monkeypatch.setattr(InspectionApi, "inspection_status_list", api_mock)

    assert isinstance(
        vue_avis_client.get_inspection_result(inspection_id=1), CommandFailedResponse
    )

    assert 3 == api_mock.call_count


def test_retries_api_failure_add_image_to_inspection(
    monkeypatch, vue_avis_client, image_file
):
    api_mock = MagicMock(side_effect=ApiException(reason="API failure", status=500))
    monkeypatch.setattr(ImageApi, "image_create", api_mock)

    assert isinstance(
        vue_avis_client.add_image_to_inspection(inspection_id=1, image=image_file),
        CommandFailedResponse,
    )

    assert 3 == api_mock.call_count
