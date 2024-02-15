from unittest.mock import MagicMock, Mock, patch

import pytest
from avis_agent.core.base import Agent
from avis_agent.core.commands import (
    AddImageCommand,
    ReadyCommand,
    StartInspectionCommand,
)
from avis_agent.core.exceptions import AgentError
from avis_agent.core.responses import (
    CommandFailedResponse,
    CommandSuccessfulResponse,
    ReadyResponse,
)
from PIL import Image


@pytest.fixture
def mock_camera(screw_image):
    camera = MagicMock()
    camera.capture_image.return_value = screw_image
    return camera


@pytest.fixture
def mock_backend():
    return MagicMock()


@pytest.fixture
def mock_signal():
    return MagicMock()


@pytest.fixture
def image_path(tmp_path):
    return tmp_path / "image.png"


@pytest.fixture
def mock_config(image_path):
    config = MagicMock()
    config.instrumentation = None
    config.camera.image_path = image_path
    return config


@pytest.fixture
def mock_agent(mock_camera, mock_backend, mock_signal, mock_config):
    return Agent(mock_backend, mock_camera, mock_signal, mock_config)


def test_command_checkpoint_initialized(mock_agent):
    inspection_id = 1
    commands_to_read = [
        ReadyCommand(),
        StartInspectionCommand(),
        Exception("Simulated exit"),
    ]
    mock_agent.signal.read.side_effect = commands_to_read
    mock_agent.backend.execute.side_effect = [
        ReadyResponse(),
        CommandSuccessfulResponse(
            result=inspection_id, message="Inspection successfully created"
        ),
    ]

    with pytest.raises(Exception, match="Simulated exit"):
        mock_agent.run()

    assert mock_agent.current_inspection_id == inspection_id
    assert mock_agent.last_command == commands_to_read[1]


def test_command_checkpoint_gets_updated(mock_agent):
    inspection_id = 1
    commands_to_read = [
        ReadyCommand(),
        StartInspectionCommand(),
        ReadyCommand(),
        AddImageCommand(inspection_id=inspection_id),
        Exception("Simulated exit"),
    ]
    mock_agent.signal.read.side_effect = commands_to_read
    mock_agent.backend.execute.side_effect = [
        ReadyResponse(),
        CommandSuccessfulResponse(
            result=inspection_id, message="Inspection successfully created"
        ),
        ReadyResponse(),
        CommandSuccessfulResponse(message="Image added to inspection"),
    ]

    with pytest.raises(Exception, match="Simulated exit"):
        mock_agent.run()

    assert mock_agent.current_inspection_id == inspection_id
    assert mock_agent.last_command == commands_to_read[3]


def test_command_checkpoint_inspection_id_get_updated(mock_agent):
    first_inspection_id = 1
    second_inspection_id = 2

    commands_to_read = [
        ReadyCommand(),
        StartInspectionCommand(),
        ReadyCommand(),
        StartInspectionCommand(),
        Exception("Simulated exit"),
    ]
    mock_agent.signal.read.side_effect = commands_to_read
    mock_agent.backend.execute.side_effect = [
        ReadyResponse(),
        CommandSuccessfulResponse(
            result=first_inspection_id, message="Inspection successfully created"
        ),
        ReadyResponse(),
        CommandSuccessfulResponse(
            result=second_inspection_id, message="Inspection successfully created"
        ),
    ]

    with pytest.raises(Exception, match="Simulated exit"):
        mock_agent.run()

    assert mock_agent.current_inspection_id == second_inspection_id
    assert mock_agent.last_command == commands_to_read[3]


def test_process_command_add_image(mock_agent, image_path, screw_image):
    command = AddImageCommand(inspection_id=1, image=image_path)
    mock_agent.camera.check_camera_ready.return_value = True
    mock_agent.last_command = ReadyCommand()
    result = mock_agent._pre_process(command)

    assert hasattr(result, "image")
    assert result.image == image_path
    assert Image.open(result.image) == screw_image


def test_process_command_camera_not_ready(mock_agent):
    command = AddImageCommand()
    mock_agent.camera.check_camera_ready.return_value = False

    result = mock_agent._process_command(command)
    assert isinstance(result, AgentError)


def test_agent_starts_camera_correctly(mock_agent):
    mock_agent.signal.read.side_effect = [ReadyCommand(), Exception("Simulated exit")]
    with pytest.raises(Exception, match="Simulated exit"):
        mock_agent.run()
    mock_agent.camera.start.assert_called_once()


def test_agent_handles_camera_start_error(mock_agent):
    error = AgentError("Camera start error")
    mock_agent.camera.start.return_value = error

    with patch(
        "avis_agent.core.base.Agent._process_command", return_value=ReadyCommand()
    ):
        mock_agent.run()

    mock_agent.signal.write.assert_called_once_with(error)


def test_agent_wait_until_ready(mock_agent):
    mock_agent.signal.read.side_effect = [
        StartInspectionCommand(),  # not ready
        AddImageCommand(),  # not ready
        ReadyCommand(),  # ready
        StartInspectionCommand(),
        Exception("Simulated exit"),
    ]

    with pytest.raises(Exception, match="Simulated exit"):
        mock_agent.run()

    mock_agent.backend.execute.assert_called_with(StartInspectionCommand())


def test_agent_inspection_id_not_set(mock_agent):
    mock_agent.current_inspection_id = None
    mock_agent.signal.read.side_effect = [
        ReadyCommand(),
        AddImageCommand(),
        Exception("Simulated exit"),
    ]

    with pytest.raises(Exception, match="Simulated exit"):
        mock_agent.run()

    mock_agent.signal.write.assert_called_with(
        AgentError("The inspection ID is not known.")
    )


def test_agent_handles_camera_not_ready(mock_agent):
    error = AgentError("Camera is not ready")
    mock_agent.camera.check_camera_ready.return_value = False
    mock_agent.current_inspection_id = 1
    mock_agent.signal.read.side_effect = [
        ReadyCommand(),
        AddImageCommand(),
        Exception("Simulated exit"),
    ]

    with pytest.raises(Exception, match="Simulated exit"):
        mock_agent.run()

    mock_agent.signal.write.assert_called_with(error)


def test_agent_handles_image_capture_error(mock_agent):
    error = AgentError("Image capture error")
    mock_agent.camera.capture_image.return_value = error
    mock_agent.current_inspection_id = 1
    mock_agent.signal.read.side_effect = [
        ReadyCommand(),
        AddImageCommand(inspection_id=1),
        Exception("Simulated exit"),
    ]

    with pytest.raises(Exception, match="Simulated exit"):
        mock_agent.run()

    mock_agent.signal.write.assert_called_with(error)


def test_signal_close_is_called_when_agent_exits(mock_agent):
    mock_agent.signal.read.side_effect = [
        ReadyCommand(),
        Exception("Simulated exit"),
    ]

    with pytest.raises(Exception, match="Simulated exit"):
        mock_agent.run()

    mock_agent.signal.close.assert_called_once()


def test_agent_should_should_not_revert_to_ready_when_last_command_failed_and_there_was_no_acknowledgement(
    mock_agent,
):
    mock_agent.signal.read.side_effect = [
        ReadyCommand(),
        StartInspectionCommand(),
        ReadyCommand(),
        AddImageCommand(),
        StartInspectionCommand(),
        Exception("Simulated exit"),
    ]
    mock_agent._handle_command = Mock(
        side_effect=[
            ReadyResponse(),
            CommandSuccessfulResponse(
                result=1, message="Inspection successfully created"
            ),
            ReadyResponse(),
            CommandFailedResponse(result=None, message="Simulated error"),
        ]
    )

    with pytest.raises(Exception, match="Simulated exit"):
        mock_agent.run()

    assert type(mock_agent.last_command) == AddImageCommand
    assert mock_agent.current_inspection_id == 1


def test_acknowledgment_after_failure(mock_agent):
    mock_agent.signal.read.side_effect = [
        ReadyCommand(),
        StartInspectionCommand(),
        ReadyCommand(),
        AddImageCommand(),
        ReadyCommand(),
        StartInspectionCommand(),
        Exception("Simulated exit"),
    ]
    mock_agent._handle_command = Mock(
        side_effect=[
            ReadyResponse(),
            CommandSuccessfulResponse(
                result=1, message="Inspection successfully created"
            ),
            ReadyResponse(),
            CommandFailedResponse(result=None, message="Simulated error"),
            ReadyResponse(),
            CommandSuccessfulResponse(
                result=2, message="Inspection successfully created"
            ),
            ReadyResponse(),
        ]
    )

    with pytest.raises(Exception, match="Simulated exit"):
        mock_agent.run()

    assert type(mock_agent.last_command) == StartInspectionCommand
    assert mock_agent.current_inspection_id == 2


def test_agent_should_revert_to_ready_when_failure_was_acknowledged(mock_agent):
    mock_agent.signal.read.side_effect = [
        ReadyCommand(),
        AddImageCommand(),
        ReadyCommand(),
        Exception("Simulated exit"),
    ]
    mock_agent._handle_command = Mock(
        side_effect=[
            ReadyResponse(),
            CommandFailedResponse(result=None, message="Simulated error"),
            ReadyResponse(),
        ]
    )

    with pytest.raises(Exception, match="Simulated exit"):
        mock_agent.run()

    assert type(mock_agent.last_command) == ReadyCommand
    assert type(mock_agent.last_response) == ReadyResponse
