"""A logging handler that uses Loguru for logging."""

from loguru import logger

from yaplogger.handlers.base_handler import BaseHandler


class LoguruHandler(BaseHandler):
    """A logging handler that uses Loguru for logging."""

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
