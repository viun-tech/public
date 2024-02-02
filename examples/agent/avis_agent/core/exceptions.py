class CommandUnknown(Exception):
    """Exception raised when a command is unknown."""


class ResponseUnknown(Exception):
    """Exception raised when a response is unknown."""


class AgentError(Exception):
    """
    General exception raised when an error occurs in the agent.
    """

    def __eq__(self, other):
        if isinstance(other, AgentError):
            return str(self) == str(other)
        return False
