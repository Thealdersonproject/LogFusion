"""Abstract base class for logging handlers.

This module provides an abstract base class (`BaseHandler`) for logging handlers.
The `BaseHandler` class defines the interface for logging handlers, requiring
implementations of methods for logging messages at various severity levels.
This class is designed to be subclassed to create custom logging handlers.

Classes:
    - BaseHandler: Abstract base class for logging handlers.

Usage:
    To create a custom logging handler, subclass the `BaseHandler` class and
    implement its abstract methods.

Example:
    ```python
    from handlers.base_handler import BaseHandler


    class CustomHandler(BaseHandler):
        def debug(self, message: str) -> None:
            # Custom implementation for debug logging
            pass

        def info(self, message: str) -> None:
            # Custom implementation for info logging
            pass

        def warning(self, message: str) -> None:
            # Custom implementation for warning logging
            pass

        def error(self, message: str) -> None:
            # Custom implementation for error logging
            pass

        def critical(self, message: str) -> None:
            # Custom implementation for critical logging
            pass

        def exception(self, message: str, exc_info: Exception) -> None:
            # Custom implementation for exception logging
            pass
    ```
"""

from abc import ABC, abstractmethod


class BaseHandler(ABC):
    """Base class for logging different levels of messages.

    This abstract base class provides methods to log messages at various
    severity levels such as debug, info, warning, error, critical, and
    exceptions. Subclasses must implement these methods to provide specific
    logging functionality. This allows consistent logging interface that can
    be extended or customized as needed.
    """

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
