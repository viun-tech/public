from abc import ABC, abstractmethod
from pathlib import Path
from typing import Union

from avis_agent.core.exceptions import AgentError
from pydantic import BaseModel


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


class StartInspectionCommand(AbstractCommand):
    """
    Start a new inspection. The agent should return a StartinspectionResponseSuccessful with the inspection id when the inspection is started.
    """

    def __str__(self):
        return f"{self.__class__.__name__}()"


class AddImageCommand(AbstractCommand):
    """
    Add an image to a inspection. The agent should return a AddImageResponseSuccessful with the image id when the image is
    added.
    """

    inspection_id: Union[int, None] = None
    image: Union[Path, None] = None

    def __str__(self):
        return f"{self.__class__.__name__}(inspection_id={self.inspection_id})"


class GetInspectionResultCommand(AbstractCommand):
    """
    Get the inspection result for a inspection. The agent should return either a QualityTestSuccessfulResponse,
    a QualityTestFailedResponse or a QualityTestUncertainResponse.
    """

    inspection_id: Union[int, None] = None

    def __str__(self):
        return f"{self.__class__.__name__}(inspection_id={self.inspection_id})"


class AbstractCommandReader(ABC):
    @abstractmethod
    def read(self, *args, **kwargs) -> Union[AbstractCommand, AgentError]:
        ...


# require a inspection id
StatefulCommandTypes = (AddImageCommand, GetInspectionResultCommand)
