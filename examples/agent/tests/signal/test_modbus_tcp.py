import pytest
from avis_agent.core.commands import (
    AddImageCommand,
    GetInspectionResultCommand,
    ReadyCommand,
    StartInspectionCommand,
)
from avis_agent.core.exceptions import AgentError
from avis_agent.core.responses import (
    CommandFailedResponse,
    CommandSuccessfulResponse,
    QualityTestFailedResponse,
    QualityTestSuccessfulResponse,
    QualityTestUncertainResponse,
    ReadyResponse,
)
from avis_agent.signal.impl.modbus_tcp import (
    CommandCoilSettings,
    ModbusTcpCommandReader,
    ModbusTcpResponseWriter,
    ModbusTcpSignal,
    ModbusTcpSignalSettings,
    ResponseCoilSettings,
)


@pytest.fixture(autouse=True)
def clean_up(reset_coils_after_test):
    yield


@pytest.fixture
def modbus_config(
    modbus_server: None, modbus_server_port: int
) -> ModbusTcpSignalSettings:
    return ModbusTcpSignalSettings(
        name="modbus_tcp",
        host="localhost",
        port=modbus_server_port,
    )


def verify_ready_coil(coils):
    assert coils[0]
    assert sum(coils) == 1


# Parametrize command tests
@pytest.mark.parametrize(
    "coil, command_type",
    [
        (1, StartInspectionCommand),
        (2, AddImageCommand),
        (3, GetInspectionResultCommand),
    ],
)
def test_read_commands(modbus_config, modbus_client, coil, command_type):
    modbus_client.write_coil(0, True)
    reader = ModbusTcpCommandReader(modbus_config)
    assert isinstance(reader.read(), ReadyCommand)
    modbus_client.write_coil(coil, True)
    assert isinstance(reader.read(), command_type)


# Parametrize response tests
@pytest.mark.parametrize(
    "coil, response_type",
    [
        (5, CommandSuccessfulResponse),
        (6, CommandFailedResponse),
        (7, QualityTestSuccessfulResponse),
        (8, QualityTestFailedResponse),
        (9, QualityTestUncertainResponse),
    ],
)
def test_write_responses(modbus_config, modbus_client, coil, response_type):
    writer = ModbusTcpResponseWriter(modbus_config)
    verify_ready_coil(modbus_client.read_coils(4, 4).bits[:4])
    assert writer.write(response_type(message="Test message"))
    coils = modbus_client.read_coils(0, 10).bits[:10]
    # verify that the ready coil and the correct response coils are set
    assert coils[4] and coils[coil] and sum(coils) == 2


def test_modbus_signal(modbus_config, modbus_client):
    signal = ModbusTcpSignal(
        modbus_config,
    )
    verify_ready_coil(modbus_client.read_coils(4, 4).bits[:4])
    modbus_client.write_coil(0, True)
    assert isinstance(signal.read(), ReadyCommand)
    modbus_client.write_coil(1, True)
    assert isinstance(signal.read(), StartInspectionCommand)
    assert signal.write(CommandSuccessfulResponse(message="Test message"))
    coils = modbus_client.read_coils(4, 4).bits[:4]
    assert coils[0] and coils[1] and sum(coils) == 2


def test_agenterror_results_in_ready_state(modbus_config, modbus_client):
    signal = ModbusTcpSignal(
        modbus_config,
    )
    verify_ready_coil(modbus_client.read_coils(4, 4).bits[:4])
    assert signal.write(AgentError("Error"))
    # agent coils
    coils = modbus_client.read_coils(4, 4).bits[:4]
    # verify that the ready coil and command failed coils are written
    assert coils[0] and coils[2] and sum(coils) == 2


def test_all_coils_are_off_when_signal_is_closed(modbus_config, modbus_client):
    signal = ModbusTcpSignal(
        modbus_config,
    )
    verify_ready_coil(modbus_client.read_coils(4, 4).bits[:4])
    assert signal.write(CommandSuccessfulResponse(message="Test message"))
    # agent coils
    coils = modbus_client.read_coils(4, 4).bits[:4]
    # check that the ready and command successful coils are set
    assert coils[0] and coils[1] and sum(coils) == 2
    signal.close()
    # check that all coils are off
    coils = modbus_client.read_coils(4, 4).bits[:4]
    assert sum(coils) == 0


def test_wait_for_command_when_other_party_is_not_ready(modbus_config, modbus_client):
    signal = ModbusTcpSignal(
        modbus_config,
    )
    verify_ready_coil(modbus_client.read_coils(4, 4).bits[:4])
    # ready coil of the other party is off
    modbus_client.write_coil(0, False)
    assert isinstance(signal.read(), ReadyCommand)
    coils = modbus_client.read_coils(0, 8).bits
    # verify that the agent is ready and the other party is not
    assert not coils[0] and coils[4] and sum(coils) == 1


def test_revert_to_ready_and_wait_when_other_party_is_offline(
    modbus_config, modbus_client
):
    signal = ModbusTcpSignal(
        modbus_config,
    )
    verify_ready_coil(modbus_client.read_coils(4, 4).bits[:4])
    # ready coil of the other party is on
    modbus_client.write_coil(0, True)
    assert isinstance(signal.read(), ReadyCommand)
    # start inspection
    modbus_client.write_coil(1, True)
    assert isinstance(signal.read(), StartInspectionCommand)
    assert signal.write(CommandSuccessfulResponse(message="Test message"))
    # other party goes offline
    modbus_client.write_coil(0, False)
    # check that we reverted to ready and idle
    assert isinstance(signal.read(), ReadyCommand)
    assert signal.write(ReadyResponse())
    coils = modbus_client.read_coils(0, 8).bits
    # other party command coil on but ready coil off
    assert not coils[0] and coils[1]
    # agent ready coil on
    assert coils[4]
    assert sum(coils) == 2


def test_contiguous_modbus_coil_settings(modbus_config, modbus_client):
    command_coil_settings = CommandCoilSettings(
        coil_mapping={
            ReadyCommand: 4,
            StartInspectionCommand: 5,
            AddImageCommand: 6,
            GetInspectionResultCommand: 7,
        }
    )

    response_coil_settings = ResponseCoilSettings(
        coil_mapping={
            ReadyResponse: 8,
            CommandSuccessfulResponse: 9,
            CommandFailedResponse: 10,
            QualityTestSuccessfulResponse: 9,
            QualityTestFailedResponse: 11,
            QualityTestUncertainResponse: 12,
        },
    )

    modbus_config.command_coil_settings = command_coil_settings
    modbus_config.response_coil_settings = response_coil_settings

    signal = ModbusTcpSignal(
        modbus_config,
    )

    # verify that the ready coil is set
    assert modbus_client.read_coils(response_coil_settings.ready_coil_idx, 1).bits[0]

    modbus_client.write_coil(4, True)
    assert isinstance(signal.read(), ReadyCommand)
    modbus_client.write_coil(5, True)
    assert isinstance(signal.read(), StartInspectionCommand)
    assert signal.write(CommandSuccessfulResponse(message="Test message"))
    machine_ready_coil = modbus_client.read_coils(4, 1).bits[0]
    machine_start_inspection_coil = modbus_client.read_coils(5, 1).bits[0]
    coils = modbus_client.read_coils(8, 4).bits[:4]
    assert machine_ready_coil and machine_start_inspection_coil and sum(coils) == 2

    coils = modbus_client.read_coils(8, 4).bits[:4]
    assert coils[0] and coils[1] and sum(coils) == 2


def test_non_contiguous_coil_settings(modbus_config, modbus_client):
    command_coil_settings = CommandCoilSettings(
        coil_mapping={
            ReadyCommand: 4,
            StartInspectionCommand: 8,
            AddImageCommand: 12,
            GetInspectionResultCommand: 16,
        }
    )

    response_coil_settings = ResponseCoilSettings(
        coil_mapping={
            ReadyResponse: 5,
            CommandSuccessfulResponse: 9,
            CommandFailedResponse: 13,
            QualityTestSuccessfulResponse: 9,
            QualityTestFailedResponse: 17,
            QualityTestUncertainResponse: 21,
        }
    )

    modbus_config.command_coil_settings = command_coil_settings
    modbus_config.response_coil_settings = response_coil_settings

    signal = ModbusTcpSignal(
        modbus_config,
    )

    # verify that the ready coil is set
    assert modbus_client.read_coils(5, 1).bits[0]
    # verify that the other coils are not set
    assert not modbus_client.read_coils(9, 1).bits[0]
    assert not modbus_client.read_coils(13, 1).bits[0]
    assert not modbus_client.read_coils(17, 1).bits[0]
    assert not modbus_client.read_coils(21, 1).bits[0]

    modbus_client.write_coil(4, True)
    assert isinstance(signal.read(), ReadyCommand)
    modbus_client.write_coil(8, True)
    assert isinstance(signal.read(), StartInspectionCommand)
    assert signal.write(CommandSuccessfulResponse(message="Test message"))

    machine_ready_coil = modbus_client.read_coils(4, 1).bits[0]
    machine_start_inspection_coil = modbus_client.read_coils(8, 1).bits[0]
    machine_add_image_coil = modbus_client.read_coils(12, 1).bits[0]
    machine_get_inspection_result_coil = modbus_client.read_coils(13, 1).bits[0]
    assert (
        machine_ready_coil
        and machine_start_inspection_coil
        and not machine_add_image_coil
        and not machine_get_inspection_result_coil
    )

    agent_ready_coil = modbus_client.read_coils(5, 1).bits[0]
    agent_command_successful_coil = modbus_client.read_coils(9, 1).bits[0]
    agent_command_failed_coil = modbus_client.read_coils(13, 1).bits[0]
    agent_quality_test_failed_coil = modbus_client.read_coils(17, 1).bits[0]
    agent_quality_test_uncertain_coil = modbus_client.read_coils(21, 1).bits[0]
    assert (
        agent_ready_coil
        and agent_command_successful_coil
        and not agent_command_failed_coil
        and not agent_quality_test_failed_coil
        and not agent_quality_test_uncertain_coil
    )


def test_command_failed_coil_should_be_turned_off_when_failure_has_been_acknowledged(
    modbus_config, modbus_client
):
    signal = ModbusTcpSignal(
        modbus_config,
    )
    verify_ready_coil(modbus_client.read_coils(4, 4).bits[:4])
    # ready coil of the other party is on
    modbus_client.write_coil(0, True)
    assert isinstance(signal.read(), ReadyCommand)
    # start inspection
    modbus_client.write_coil(1, True)
    assert isinstance(signal.read(), StartInspectionCommand)
    assert signal.write(CommandFailedResponse(message="Test message"))
    # check failure coil is set
    assert modbus_client.read_coils(6, 1).bits[0]
    # other party acknowledges failure by turning off command coil
    modbus_client.write_coil(1, False)
    assert isinstance(signal.read(), ReadyCommand)
    # check failure coil is off
    assert not modbus_client.read_coils(6, 1).bits[0]
    # check that we reverted to ready and idle
    assert isinstance(signal.read(), ReadyCommand)
