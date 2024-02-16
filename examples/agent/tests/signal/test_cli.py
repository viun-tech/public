from unittest.mock import MagicMock

import pytest
from avis_agent.core.commands import (
    AddImageCommand,
    GetInspectionResultCommand,
    StartInspectionCommand,
)
from avis_agent.core.responses import (
    CommandFailedResponse,
    CommandSuccessfulResponse,
    QualityTestFailedResponse,
)
from avis_agent.signal.impl.cli import CliCommandReader, CliResponseWriter, CliSignal


@pytest.fixture
def cli_config():
    return MagicMock()


@pytest.mark.parametrize(
    "command, expected_output",
    [
        ("startinspection", StartInspectionCommand),
        ("addimage", AddImageCommand),
        ("getinspectionresult", GetInspectionResultCommand),
    ],
)
def test_cli_command_dispatch(command, expected_output, cli_config):
    reader = CliCommandReader(cli_config)
    assert isinstance(reader.read(command), expected_output)


@pytest.mark.parametrize(
    "response, expected_output",
    [
        (CommandSuccessfulResponse(message="Test message"), "Test message\n"),
        (CommandFailedResponse(message="Test message"), "Test message\n"),
        (QualityTestFailedResponse(message="Test message"), "Test message\n"),
    ],
)
def test_cli_response_writer(response, expected_output, capfd, cli_config):
    writer = CliResponseWriter(cli_config)
    writer.write(response)
    out, err = capfd.readouterr()
    assert out == expected_output


@pytest.mark.parametrize(
    "user_input, expected_type",
    [
        ("startinspection", StartInspectionCommand),
        ("addimage", AddImageCommand),
        ("getinspectionresult", GetInspectionResultCommand),
    ],
)
def test_cli_signal_read(user_input, expected_type, monkeypatch, cli_config):
    signal = CliSignal(cli_config)
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    assert isinstance(signal.read(), expected_type)


@pytest.mark.parametrize(
    "response, expected_output",
    [
        (CommandSuccessfulResponse(message="Test message"), "Test message\n"),
        (CommandFailedResponse(message="Test message"), "Test message\n"),
        (QualityTestFailedResponse(message="Test message"), "Test message\n"),
    ],
)
def test_cli_signal_write(response, expected_output, capfd, cli_config):
    signal = CliSignal(cli_config)
    assert signal.write(response)
    out, err = capfd.readouterr()
    assert out == expected_output
