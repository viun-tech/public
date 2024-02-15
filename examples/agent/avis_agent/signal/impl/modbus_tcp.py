import logging
import sys
from typing import Any, Dict, Literal, Type, Union

from avis_agent.core.commands import (
    AbstractCommand,
    AbstractCommandReader,
    AddImageCommand,
    GetInspectionResultCommand,
    ReadyCommand,
    StartInspectionCommand,
)
from avis_agent.core.exceptions import AgentError
from avis_agent.core.responses import (
    AbstractResponse,
    AbstractResponseWriter,
    CommandFailedResponse,
    CommandSuccessfulResponse,
    QualityTestFailedResponse,
    QualityTestSuccessfulResponse,
    QualityTestUncertainResponse,
    ReadyResponse,
)
from avis_agent.signal.base import AbstractSignal, BaseSignalSettings
from pydantic import model_validator
from pydantic_settings import BaseSettings
from pymodbus.client import ModbusTcpClient

logger = logging.getLogger(__name__)


def get_classes_for_coil_mapping(data: Any, module: str) -> Any:
    """
    Get the python class for the coil mapping from a string.

    Can be used as is as a model validator for pydantic models.

    Args:
        data: The data to validate.
        module: The module to look for the classes in.

    Returns: The validated data.
    """
    if isinstance(data, dict) and data:
        out = {}
        for command, coil in data["coil_mapping"].items():
            if isinstance(command, str):
                out[getattr(sys.modules[module], command)] = coil
            else:
                out[command] = coil
        data["coil_mapping"] = out
    return data


class CommandCoilSettings(BaseSettings):
    coil_mapping: Dict[Type[AbstractCommand], int] = {
        ReadyCommand: 0,
        StartInspectionCommand: 1,
        AddImageCommand: 2,
        GetInspectionResultCommand: 3,
    }

    @property
    def ready_coil_idx(self):
        return self.coil_mapping[ReadyCommand]

    @model_validator(mode="before")
    @classmethod
    def get_class(cls, data: Any) -> Any:
        return get_classes_for_coil_mapping(data, "avis_agent.core.commands")


class ResponseCoilSettings(BaseSettings):
    coil_mapping: Dict[Type[AbstractResponse], int] = {
        ReadyResponse: 4,
        CommandSuccessfulResponse: 5,
        CommandFailedResponse: 6,
        QualityTestSuccessfulResponse: 7,
        QualityTestFailedResponse: 8,
        QualityTestUncertainResponse: 9,
    }

    @property
    def ready_coil_idx(self):
        return self.coil_mapping[ReadyResponse]

    @property
    def failed_response_coil_idx(self):
        return self.coil_mapping[CommandFailedResponse]

    @model_validator(mode="before")
    @classmethod
    def get_class(cls, data: Any) -> Any:
        return get_classes_for_coil_mapping(data, "avis_agent.core.responses")


class ModbusTcpSignalSettings(BaseSignalSettings):
    name: Literal["modbus_tcp"]
    host: str
    port: int
    command_coil_settings: CommandCoilSettings = CommandCoilSettings()
    response_coil_settings: ResponseCoilSettings = ResponseCoilSettings()


class ModbusTcpCommandReader(AbstractCommandReader):
    def __init__(self, config: ModbusTcpSignalSettings) -> None:
        self.config = config
        self.modbus_client = ModbusTcpClient(config.host, port=config.port)

    def is_coil_set(self, coil_id: int) -> bool:
        """Check if a coil is set"""
        return self.modbus_client.read_coils(coil_id, 1).bits[0]

    def read(self) -> Union[AbstractCommand, AgentError]:
        try:
            if not self.is_coil_set(
                self.config.command_coil_settings.coil_mapping[ReadyCommand]
            ):
                # if the other party is not ready or is suddenly offline we just revert everything
                # to ready state
                return ReadyCommand()
            for (
                command_class,
                coil_id,
            ) in self.config.command_coil_settings.coil_mapping.items():
                if command_class is not ReadyCommand and self.is_coil_set(coil_id):
                    return command_class()
            # if there was a failure and the other party is ready again (acknowledged by turning off the command coil)
            # we set the response failed coils to off
            if self.is_coil_set(
                self.config.response_coil_settings.ready_coil_idx
            ) and self.is_coil_set(
                self.config.response_coil_settings.failed_response_coil_idx
            ):
                self.modbus_client.write_coil(
                    self.config.response_coil_settings.failed_response_coil_idx, False
                )
            return ReadyCommand()
        except Exception as e:
            logger.error(f"({type(e).__name__}) {e}")
            return AgentError(f"({type(e).__name__}) {e}")
        finally:
            self.modbus_client.close()

    def clear(self) -> None:
        pass


class ModbusTcpResponseWriter(AbstractResponseWriter):
    def __init__(self, config: ModbusTcpSignalSettings) -> None:
        self.config = config
        self.modbus_client = ModbusTcpClient(config.host, port=config.port)
        self.revert_to_ready()

    def write_commandfailed_response(self) -> None:
        """Write a command failed response to the modbus tcp server"""
        self.modbus_client.write_coil(
            self.config.response_coil_settings.coil_mapping[CommandFailedResponse], True
        )

    def revert_to_ready(self) -> None:
        """Revert to ready state: turn off all response coils but leave ready coil on"""
        for coil_id in self.config.response_coil_settings.coil_mapping.values():
            self.modbus_client.write_coil(coil_id, False)
        self.modbus_client.write_coil(
            self.config.response_coil_settings.coil_mapping[ReadyResponse], True
        )

    def turn_off_all_coils(self) -> None:
        """Turn off all coils (ready coil is turned off last)"""
        for coil_id in self.config.response_coil_settings.coil_mapping.values():
            self.modbus_client.write_coil(coil_id, False)

    def write(self, response: AbstractResponse) -> bool:
        try:
            if type(response) is AgentError:
                self.config.with_retries(self.write_commandfailed_response)
            elif type(response) is ReadyResponse:
                self.config.with_retries(self.revert_to_ready)
            else:
                coil_id = self.config.response_coil_settings.coil_mapping[
                    type(response)
                ]
                self.config.with_retries(self.modbus_client.write_coil, coil_id, True)
            return True
        except Exception as e:
            logger.error(f"({type(e).__name__}) {e}")
            self.config.with_retries(self.write_commandfailed_response)
            return False
        finally:
            self.modbus_client.close()

    def close(self) -> None:
        self.config.with_retries(self.turn_off_all_coils)


class ModbusTcpSignal(AbstractSignal):
    def __init__(
        self,
        config: ModbusTcpSignalSettings,
    ) -> None:
        command_reader = ModbusTcpCommandReader(config)
        response_writer = ModbusTcpResponseWriter(config)
        super().__init__(command_reader, response_writer, config)
