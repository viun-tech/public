import os

import pytest
from avis_agent.core.base import Agent, AgentSettings
from avis_agent.core.commands import (
    AddImageCommand,
    GetCaseInspectionResultCommand,
    ReadyCommand,
    StartCaseCommand,
)
from avis_agent.core.responses import (
    CommandFailedResponse,
    CommandSuccessfulResponse,
    QualityTestFailedResponse,
    QualityTestUncertainResponse,
    ReadyResponse,
)
from avis_agent.main import main


@pytest.fixture(autouse=True)
def mockreturn(monkeypatch):
    monkeypatch.setattr(Agent, "run", lambda x: None)


@pytest.fixture
def runner():
    from click.testing import CliRunner

    return CliRunner()


@pytest.fixture
def expected_config() -> str:
    return (
        "Starting agent with config: timeout=10.0 max_retries=3 wait_fixed=1.0 "
        "wait_random=(0.0, 1.5) camera=MockCameraSettings(timeout=10.0, "
        "max_retries=3, wait_fixed=1.0, wait_random=(0.0, 1.5), name='mock', "
        "image_path=PosixPath('test')) backend=AvisBackendSettings(timeout=10.0, "
        "max_retries=3, wait_fixed=1.0, wait_random=(0.0, 1.5), name='avis', "
        "api_key='test', team_id=1, inspection_object_id=1, uri='test') "
        "signal=CliSignalSettings(timeout=10.0, max_retries=3, wait_fixed=1.0, "
        "wait_random=(0.0, 1.5), name='cli', polling_interval=0.1) "
        "instrumentation=None\n"
    )


def test_config_env_file_loaded(runner, shared_datadir, expected_config):
    result = runner.invoke(main, ["--config", shared_datadir / "test_config.env"])
    assert expected_config in result.output


def test_config_json_file_loaded(runner, shared_datadir, expected_config):
    result = runner.invoke(main, ["--config", shared_datadir / "test_config.json"])
    assert expected_config in result.output


def test_coil_mapping_config():
    os.environ["AGENT_CAMERA"] = '{"name": "mock", "image_path": "image.png"}'
    os.environ[
        "AGENT_BACKEND"
    ] = '{"name": "avis", "api_key": "", "team_id": 1, "inspection_object_id": 1, "uri": ""}'
    os.environ["AGENT_SIGNAL"] = """{
        "name": "modbus_tcp",
        "host": "localhost",
        "port": 502,
        "command_coil_settings": {
            "coil_mapping": {
                "ReadyCommand": 12,
                "StartCaseCommand": 13,
                "AddImageCommand": 14,
                "GetCaseInspectionResultCommand": 15
            }
        },
        "response_coil_settings": {
            "coil_mapping": {
                "ReadyResponse": 16,
                "CommandSuccessfulResponse": 17,
                "CommandFailedResponse": 18,
                "QualityTestFailedResponse": 19,
                "QualityTestUncertainResponse": 20
            }
        }
    }"""
    settings = AgentSettings().signal
    assert settings.command_coil_settings.coil_mapping[ReadyCommand] == 12
    assert settings.command_coil_settings.coil_mapping[StartCaseCommand] == 13
    assert settings.command_coil_settings.coil_mapping[AddImageCommand] == 14
    assert (
        settings.command_coil_settings.coil_mapping[GetCaseInspectionResultCommand]
        == 15
    )
    assert settings.response_coil_settings.coil_mapping[ReadyResponse] == 16
    assert settings.response_coil_settings.coil_mapping[CommandSuccessfulResponse] == 17
    assert settings.response_coil_settings.coil_mapping[CommandFailedResponse] == 18
    assert settings.response_coil_settings.coil_mapping[QualityTestFailedResponse] == 19
    assert (
        settings.response_coil_settings.coil_mapping[QualityTestUncertainResponse] == 20
    )
    assert settings.host == "localhost"
    assert settings.port == 502
