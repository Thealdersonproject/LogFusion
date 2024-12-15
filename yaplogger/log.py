# whoami::./yaplogger/log.py
"""Instantiate, configure and retrieve the log handler from YapLogger."""

import sys
from typing import Any

from loguru import logger

from utils import singleton
from yaplogger.config import Config
from yaplogger.constants import Constants


@singleton
class Log:
    """Provides a logging class for application-wide logging functionality.

    The Log class configures the Loguru logger with specified parameters
    and ensures the logger is available for consistent usage throughout
    the application. It initializes logging configuration and provides a
    customized sink for proper formatting and output of log messages.

    Attributes:
    ----------
    configuration : dict[str, Any]
        A dictionary containing the logging parameters for configuration.
    logger : Any
        The Loguru Logger instance used for logging operations.

    Methods:
    -------
    logger
        Returns the Loguru Logger instance.
    configure_sink(**kwargs: Any)
        Configures the sink for Loguru to customize log output.
    """

    def __init__(self, parameters: dict[str, Any] | None) -> None:
        """Logger class init method."""
        self.parameters: dict[str, Any] = Config().configure(parameters=parameters)
        self._logger = logger
        self.configure_sink()

    @property
    def logger(self) -> Any:  # noqa: ANN401
        """Returns the Loguru Logger instance."""
        return self._logger

    def configure_sink(self, **kwargs: Any) -> None:  # noqa: ANN401
        """Set the configuration for loguru sink."""
        self._logger.remove(0)
        self._logger.add(
            sink=sys.stdout,
            level="INFO",
            format=Constants.STDOUT_DEFAULT_FORMAT,
            filter=None,
            colorize=True,
            serialize=False,
            backtrace=True,
            diagnose=True,
            enqueue=False,
            context=None,
            catch=True,
            **kwargs,
        )
