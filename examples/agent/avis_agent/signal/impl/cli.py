from typing import Literal, Union

from avis_agent.core.commands import (
    AbstractCommand,
    AbstractCommandReader,
    AddImageCommand,
    GetCaseInspectionResultCommand,
    ReadyCommand,
    StartCaseCommand,
)
from avis_agent.core.exceptions import AgentError
from avis_agent.core.responses import AbstractResponse, AbstractResponseWriter
from avis_agent.signal.base import AbstractSignal, BaseSignalSettings


class CliSignalSettings(BaseSignalSettings):
    name: Literal["cli"]


class CliCommandReader(AbstractCommandReader):
    def __init__(self, config: CliSignalSettings) -> None:
        self.commands = {
            "ready": ReadyCommand,
            "startcase": StartCaseCommand,
            "addimage": AddImageCommand,
            "getcaseinspectionresult": GetCaseInspectionResultCommand,
        }
        self.config = config

    def read(self, user_input: str) -> Union[AbstractCommand, AgentError]:
        try:
            return self.commands[user_input]()
        except KeyError:
            return AgentError(f"'{user_input}' is not a known command")

    def clear(self):
        pass


class CliResponseWriter(AbstractResponseWriter):
    def __init__(self, config: CliSignalSettings) -> None:
        self.config = config

    def write(self, response: AbstractResponse) -> Union[bool, AgentError]:
        if hasattr(response, "message"):
            print(response.message)
        else:
            print(response)
        return True

    def close(self):
        pass


class CliSignal(AbstractSignal):
    def __init__(
        self,
        config: CliSignalSettings,
    ) -> None:
        command_reader = CliCommandReader(config)
        response_writer = CliResponseWriter(config)
        super().__init__(command_reader, response_writer, config)

    def read(self) -> Union[AbstractCommand, AgentError]:
        user_input = input("Enter command to interact with the AVIS agent: ")
        return self.command_reader.read(user_input)

    def write(
        self, response: Union[AbstractResponse, AgentError]
    ) -> Union[bool, AgentError]:
        return self.response_writer.write(response)
