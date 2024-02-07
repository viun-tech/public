import tempfile
from unittest.mock import MagicMock

import pytest
from avis.apps.core.models import Case, Image
from avis.apps.teams.models import Team
from avis.apps.users.models import CustomUser
from avis.tests.factories import (
    make_binary_class_inspection_result,
    make_case,
    make_image,
    make_inspection_object,
)
from avis_agent.backend.impl.avis import AvisBackend, AvisBackendSettings
from avis_agent.core.exceptions import AgentError
from avis_agent.core.responses import CommandFailedResponse
from django.core.files.images import ImageFile
from pytest_django.live_server_helper import LiveServer
from vue_avis_client import ApiException, CaseApi, ImageApi

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
    inspection_object = make_inspection_object(team=test_team, save=True)
    config = AvisBackendSettings(
        name="avis",
        api_key=api_key,
        team_id=test_team.id,
        inspection_object_id=inspection_object.id,
        uri=live_server.url,
    )
    return AvisBackend(config)


def test_start_case(vue_avis_client: AvisBackend) -> None:
    response = vue_avis_client.start_case()
    assert not isinstance(response, AgentError)
    cases = Case.objects.all()
    assert len(cases) == 1
    assert cases[0].id == response.result
    assert response.message == "Case created successfully"


def test_get_case_inspection_result(
    vue_avis_client: AvisBackend,
    test_team: Team,
    user: CustomUser,
    test_image: ImageFile,
) -> None:
    inspection_result = make_binary_class_inspection_result(
        team=test_team, user=user, save=True
    )
    inspection_result.binary_class = "DEFECT"
    inspection_result.save()
    image = make_image(
        team=test_team,
        user=user,
        file=test_image,
        inspection_results=[inspection_result],
        save=True,
    )
    case = make_case(team=test_team, user=user, images=[image], save=True)
    response = vue_avis_client.get_case_inspection_result(case.id)
    assert not isinstance(response, AgentError)
    assert response.result == "DEFECT"
    assert response.message == "Case inspection status retrieved successfully"

    inspection_result.binary_class = "OK"
    inspection_result.save()

    response = vue_avis_client.get_case_inspection_result(case.id)
    assert not isinstance(response, AgentError)
    assert response.result == "OK"
    assert response.message == "Case inspection status retrieved successfully"


def test_add_image_to_case(
    vue_avis_client: AvisBackend,
    test_team: Team,
    user: CustomUser,
    image_file: str,
) -> None:
    case = make_case(team=test_team, user=user, images=[], save=True)
    assert case.images.count() == 0

    with open(image_file, "rb") as f:
        img_data = f.read()

    # add the image to the case
    response = vue_avis_client.add_image_to_case(case.id, image_file)
    assert not isinstance(response, AgentError)

    db_image = Image.objects.all()
    assert len(db_image) == 1
    assert db_image[0].id == response.result
    assert response.message == f"Image added to case {case.id} successfully"
    case.refresh_from_db()
    assert case.images.count() == 1
    assert case.images.first().file.read() == img_data


def test_retries_api_failure_start_case(monkeypatch, vue_avis_client):
    api_mock = MagicMock(side_effect=ApiException(reason="API failure", status=500))
    monkeypatch.setattr(CaseApi, "case_create", api_mock)

    assert isinstance(vue_avis_client.start_case(), CommandFailedResponse)

    assert 3 == api_mock.call_count


def test_retries_api_failure_case_inspection_result(monkeypatch, vue_avis_client):
    api_mock = MagicMock(side_effect=ApiException(reason="API failure", status=500))
    monkeypatch.setattr(CaseApi, "case_inspection_status_list", api_mock)

    assert isinstance(
        vue_avis_client.get_case_inspection_result(case_id=1), CommandFailedResponse
    )

    assert 3 == api_mock.call_count


def test_retries_api_failure_add_image_to_case(
    monkeypatch, vue_avis_client, image_file
):
    api_mock = MagicMock(side_effect=ApiException(reason="API failure", status=500))
    monkeypatch.setattr(ImageApi, "image_create", api_mock)

    assert isinstance(
        vue_avis_client.add_image_to_case(case_id=1, image=image_file),
        CommandFailedResponse,
    )

    assert 3 == api_mock.call_count
