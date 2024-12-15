# ./yaplogger/logger.py
"""A flexible logger that supports multiple logging handlers.

This module provides a `Logger` class that supports multiple logging handlers.
The `Logger` class is designed to be flexible and extensible, allowing developers to easily add new logging
handlers as needed. It includes methods for logging messages at various severity levels and supports exception logging.

Classes:
    - Logger: A flexible logger that supports multiple logging handlers.

Usage:
    ```python
    from yaplogger.logger import Logger
    from yaplogger.config import default_config

    # Initialize the logger with the default configuration
    logger = Logger(default_config)

    # Log messages at various levels
    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")

    # Log an exception
    try:
        1 / 0
    except ZeroDivisionError as e:
        logger.exception("An exception occurred", e)
    ```

Note:
    This module is part of the YapLogger project, which aims to provide a flexible and extensible logging
    framework for logging, monitoring, and observability.
"""

from typing import Any, ParamSpec

import loguru

P = ParamSpec("P")


class Logger:
    """A flexible logger that supports multiple logging handlers."""

    def __init__(self, config: dict[str, Any] | None) -> None:
        """Initialize the logger with the specified configuration.

        Args:
            config (Dict[str, Any]): The logging configuration.
        """
        self.config = config
        self._log = loguru.logger

    def debug(self, message: str) -> None:
        """Log a debug message.

        Args:
            message (str): The debug message to log.
        """
        self._log.log("DEBUG", message)

    def info(self, message: str) -> None:
        """Log an info message.

        Args:
            message (str): The info message to log.
        """
        self._log.info(message)

    def warning(self, message: str) -> None:
        """Log a warning message.

        Args:
            message (str): The warning message to log.
        """
        self._log.warning(message)

    def error(self, message: str) -> None:
        """Log an error message.

        Args:
            message (str): The error message to log.
        """
        self._log.error(message)

    def critical(self, message: str) -> None:
        """Log a critical message.

        Args:
            message (str): The critical message to log.
        """
        self._log.critical(message)

    def exception(self, message: str, *args: Any, **kwargs: Any) -> None:  # noqa: ANN401, D417
        """Log an exception message.

        Args:
            message (str): The exception message to log.
            exc_info (Exception): The exception object to log.
        """
