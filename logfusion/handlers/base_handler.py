"""Abstract base class for logging handlers."""

from abc import ABC, abstractmethod


class BaseHandler(ABC):
    """Abstract base class for logging handlers."""

    @abstractmethod
    def debug(self, message: str) -> None:
        """Log a debug message.

        Args:
            message (str): The debug message to log.
        """

    @abstractmethod
    def info(self, message: str) -> None:
        """Log an info message.

        Args:
            message (str): The info message to log.
        """

    @abstractmethod
    def warning(self, message: str) -> None:
        """Log a warning message.

        Args:
            message (str): The warning message to log.
        """

    @abstractmethod
    def error(self, message: str) -> None:
        """Log an error message.

        Args:
            message (str): The error message to log.
        """

    @abstractmethod
    def critical(self, message: str) -> None:
        """Log a critical message.

        Args:
            message (str): The critical message to log.
        """

    @abstractmethod
    def exception(self, message: str, exc_info: Exception) -> None:
        """Log an exception message.

        Args:
            message (str): The exception message to log.
            exc_info (Exception): The exception object to log.
        """