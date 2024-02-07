from typing import Any, Callable, Tuple

from pydantic_settings import BaseSettings, SettingsConfigDict
from tenacity import retry, stop_after_attempt, wait_fixed, wait_random


class BaseSettingsWithRetries(BaseSettings):
    """
    Retry settings for the agent.

    Args:
        timeout (float): The timeout in seconds.
        max_retries (int): The maximum number of retries.
        wait_fixed (float): The number of seconds to wait between retries.
        wait_random (Tuple[float, float]): Jitter to add to the wait time between retries.
    """

    timeout: float = 10
    max_retries: int = 3
    wait_fixed: float = 1
    wait_random: Tuple[float, float] = (0, 1.5)

    model_config = SettingsConfigDict(env_nested_delimiter="__")

    def with_retries(self, func: Callable[..., Any], *args, **kwargs) -> Any:
        """
        Retries the provided function call with the configured wait times and retry count.

        Args:
            func: The function to call.
            *args: Arguments to pass to the function.
            **kwargs: Keyword arguments to pass to the function.

        Returns:
            Result of the function call.
        """

        @retry(
            stop=stop_after_attempt(self.max_retries),
            wait=wait_fixed(self.wait_fixed) + wait_random(*self.wait_random),
            reraise=True,
        )
        def wrapped(*f_args, **f_kwargs):
            return func(*f_args, **f_kwargs)

        return wrapped(*args, **kwargs)
