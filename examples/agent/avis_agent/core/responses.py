from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, Union

from pydantic import BaseModel

from avis_agent.core.exceptions import AgentError

T = TypeVar("T")


class AbstractResponse(ABC, BaseModel, Generic[T]):
    message: Optional[str] = None
    result: Optional[T] = None


class CommandSuccessfulResponse(AbstractResponse[T]):
    """
    Indicates that the command was successful. The result of the command is stored in the result field.
    """

    ...


class CommandFailedResponse(AbstractResponse[None]):
    """
    Indicates that the command failed. The reason for the failure is stored in the message field.
    """

    ...


class QualityTestSuccessfulResponse(CommandSuccessfulResponse[str]):
    """
    Indicates that the quality test was successful. The result is stored in the result field.
    """

    ...


class QualityTestFailedResponse(CommandSuccessfulResponse[str]):
    """
    Indicates that the quality test failed. The result is stored in the result field.
    """

    ...


class QualityTestUncertainResponse(CommandSuccessfulResponse[str]):
    """
    Indicates that the quality test was uncertain. The result is stored in the result field.
    """

    ...


class ReadyResponse(CommandSuccessfulResponse[None]):
    """
    Indicates that the agent is ready to receive commands. Can be used as a form of acknowledgement in conjunction with
    ReadyCommand:

    >>> agent.signal.write(ReadyResponse()) # ready to receive commands
    >>> agent.signal.read() # read some command
    >>> agent.backend... # do some work
    >>> agent.signal.write(...) # write results
    >>> agent.signal.read() # read ReadyCommand meaning the other side has received the results
    >>> agent.signal.write(ReadyResponse()) # acknowledge the ReadyCommand and start again

    """

    ...


class AbstractResponseWriter(ABC):
    @abstractmethod
    def write(self, *args, **kwargs) -> Union[bool, AgentError]:
        ...

    @abstractmethod
    def close(self) -> None:
        ...
