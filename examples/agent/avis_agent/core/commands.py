from abc import ABC, abstractmethod
from pathlib import Path
from typing import Union

from pydantic import BaseModel

from avis_agent.core.exceptions import AgentError


class AbstractCommand(ABC, BaseModel):
    ...


class ReadyCommand(AbstractCommand):
    """
    Indicates that the agent is ready to receive commands. Can be used as a form of acknowledgement in
    conjunction with ReadyResponse:

    >>> agent.signal.write(ReadyResponse()) # ready to receive commands
    >>> agent.signal.read() # read some command
    >>> agent.backend... # do some work
    >>> agent.signal.write(...) # write results
    >>> agent.signal.read() # read ReadyCommand meaning the other side has received the results
    >>> agent.signal.write(ReadyResponse()) # acknowledge the ReadyCommand and start again
    """

    def __str__(self):
        return f"{self.__class__.__name__}()"


class StartCaseCommand(AbstractCommand):
    """
    Start a new case. The agent should return a StartCaseResponseSuccessful with the case id when the case is started.
    """

    def __str__(self):
        return f"{self.__class__.__name__}()"


class AddImageCommand(AbstractCommand):
    """
    Add an image to a case. The agent should return a AddImageResponseSuccessful with the image id when the image is
    added.
    """

    case_id: Union[int, None] = None
    image: Union[Path, None] = None

    def __str__(self):
        return f"{self.__class__.__name__}(case_id={self.case_id})"


class GetCaseInspectionResultCommand(AbstractCommand):
    """
    Get the inspection result for a case. The agent should return either a QualityTestSuccessfulResponse,
    a QualityTestFailedResponse or a QualityTestUncertainResponse.
    """

    case_id: Union[int, None] = None

    def __str__(self):
        return f"{self.__class__.__name__}(case_id={self.case_id})"


class AbstractCommandReader(ABC):
    @abstractmethod
    def read(self, *args, **kwargs) -> Union[AbstractCommand, AgentError]:
        ...


# require a case id
StatefulCommandTypes = (AddImageCommand, GetCaseInspectionResultCommand)
