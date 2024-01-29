from abc import ABC
from typing import Union

from avis_agent.core.commands import AbstractCommand, AbstractCommandReader
from avis_agent.core.exceptions import AgentError
from avis_agent.core.responses import AbstractResponse, AbstractResponseWriter
from avis_agent.utils import BaseSettingsWithRetries


class BaseSignalSettings(BaseSettingsWithRetries):
    name: str
    polling_interval: float = 0.1


class AbstractSignal(ABC):
    """
    Abstract representation of a Signal mechanism for the agent.

    It is used to communicate with the outside world and send/receive commands and responses.

    Different implementations of this class can be used to communicate with different systems, devices or interfaces
    using different protocols.
    """

    def __init__(
        self,
        command_reader: AbstractCommandReader,
        response_writer: AbstractResponseWriter,
        config: BaseSignalSettings,
    ) -> None:
        """
        Initialize an AbstractSignal instance.

        Args:
            command_reader: Reader used for fetching commands.
            response_writer: Writer used for sending responses.
        """
        self.command_reader = command_reader
        self.response_writer = response_writer
        self.config = config

    def read(self) -> Union[AbstractCommand, AgentError]:
        """
        Read a command using the command_reader.

        Returns:
            Union[AbstractCommand, AgentError]: The command read or an error.
        """
        return self.command_reader.read()

    def write(
        self, response: Union[AbstractResponse, AgentError]
    ) -> Union[bool, AgentError]:
        """
        Write a response using the response_writer.

        Args:
            response: The response or error to be written.

        Returns:
            Union[bool, AgentError]: Indicates success or returns an error.
        """
        return self.response_writer.write(response)

    def close(self) -> None:
        self.response_writer.close()

    @classmethod
    def build(cls, config: BaseSignalSettings):
        if config.name == "cli":
            from avis_agent.signal.impl.cli import CliSignal

            return CliSignal(config)
        elif config.name == "modbus_tcp":
            from avis_agent.signal.impl.modbus_tcp import ModbusTcpSignal

            return ModbusTcpSignal(config)
        else:
            raise ValueError(f"Unknown signal name: {config.name}")
