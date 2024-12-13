# ./yaplogger/handlers/loguru_handler.py
"""A logging handler that uses Loguru for logging.

This module provides a `LoguruHandler` class that integrates with the Loguru logging library.
The `LoguruHandler` class provides methods to log messages at various severity levels using the Loguru library.
It includes methods for debug, info, warning, error, critical, and exception logging.
The purpose of this class is to facilitate uniform logging in an application by abstracting Loguru's
logging functionality into a dedicated handler class.

Classes:
    - LoguruHandler: Handler class for integrating with the Loguru logging library.

Usage:
    ```python
    from handlers.loguru_handler import LoguruHandler

    handler = LoguruHandler()
    handler.debug("This is a debug message.")
    handler.info("This is an info message.")
    handler.warning("This is a warning message.")
    handler.error("This is an error message.")
    handler.critical("This is a critical message.")
    handler.exception("An exception occurred.", Exception("Example exception"))
    ```

Note:
    This module is part of the YapLogger project, which aims to provide a flexible and extensible logging framework for
    logging, monitoring, and observability.
"""

from loguru import logger

from . import BaseHandler


class LoguruHandler(BaseHandler):
    """Handler class for integrating with the Loguru logging library.

    This class provides methods to log messages at various severity levels
    using the Loguru library. It includes methods for debug, info, warning,
    error, critical, and exception logging. Its purpose is to facilitate
    uniform logging in an application by abstracting Loguru's logging
    functionality into a dedicated handler class.
    """

    def debug(self, message: str) -> None:
        """Log a debug message.

        Args:
            message (str): The debug message to log.
        """
        logger.debug(message)

    def info(self, message: str) -> None:
        """Log an info message.

        Args:
            message (str): The info message to log.
        """
        logger.info(message)

    def warning(self, message: str) -> None:
        """Log a warning message.

        Args:
            message (str): The warning message to log.
        """
        logger.warning(message)

    def error(self, message: str) -> None:
        """Log an error message.

        Args:
            message (str): The error message to log.
        """
        logger.error(message)

    def critical(self, message: str) -> None:
        """Log a critical message.

        Args:
            message (str): The critical message to log.
        """
        logger.critical(message)

    def exception(self, message: str, exc_info: Exception) -> None:
        """Log an exception message.

        Args:
            message (str): The exception message to log.
            exc_info (Exception): The exception object to log.
        """
        logger.exception(message, exc_info=exc_info)
