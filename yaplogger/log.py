# whoami::./yaplogger/log.py
"""Instantiate, configure and retrieve the log handler from YapLogger."""

import sys
from datetime import UTC, datetime
from typing import Any

from loguru import logger

from yaplogger.config import Config
from yaplogger.constants import Constants
from yaplogger.utils import SeverityLevel, singleton


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
        self._display_process_name: str | None = None
        self._process_UID: str | None = None
        self._start_process()

    def _start_process(self) -> None:
        """Configure sink and log information regarding the process start."""
        self._display_process_name = self.parameters[Constants.PROCESS_NAME_KEY]
        self._process_UID = self.parameters[Constants.PROCESS_UID_KEY]

        self.configure_sink()
        self.info("Process", extra_value=self._display_process_name)
        self.info("Description", extra_value=self.parameters[Constants.PROCESS_DESCRIPTION_KEY])
        self.info("Process UID", extra_value=self.parameters[Constants.PROCESS_UID_KEY])

    @property
    def logger(self) -> Any:  # noqa: ANN401
        """Returns the Loguru Logger instance."""
        return self

    def configure_sink(self, **kwargs: Any) -> None:  # noqa: ANN401
        """Set the configuration for loguru sink."""
        self._logger = logger.bind(
            process_uid=self._process_UID,
            process_name=self._display_process_name,
            display_level="",
            generated_timestamp="",
            extra_value="",
            exception_message="",
        )
        self._logger.remove(0)
        self._logger.add(
            sink=sys.stdout,
            level=SeverityLevel.INFO.name,
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

    def _log(
        self,
        level: SeverityLevel,
        message: str,
        extra_value: str | None,
        exception_message: str | Exception | None = None,
        **kwargs: Any,  # noqa: ANN401
    ) -> None:
        """Unique point to apply changes and log."""
        now: str = datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

        if exception_message:
            self._logger.log(
                level.name,
                message,
                **kwargs,
                display_level=level.name.lower(),
                generated_timestamp=now,
                exception_message=exception_message,
            )
            return

        if extra_value:
            self._logger.log(
                level.name,
                message,
                **kwargs,
                display_level=level.name.lower(),
                generated_timestamp=now,
                extra_value=extra_value,
            )
            return

        self._logger.log(
            level.name,
            message,
            **kwargs,
            display_level=level.name.lower(),
            generated_timestamp=now,
        )

    def trace(self, message: str, extra_value: str | None = None, **kwargs: Any) -> None:  # noqa: ANN401
        """Encapsulated trace method with automatic UID inclusion."""
        self._log(SeverityLevel.TRACE, message, **kwargs, extra_value=extra_value)

    def debug(self, message: str, extra_value: str | None = None, **kwargs: Any) -> None:  # noqa: ANN401
        """Encapsulated debug method with automatic UID inclusion."""
        self._log(SeverityLevel.DEBUG, message, **kwargs, extra_value=extra_value)

    def info(self, message: str, extra_value: str | None = None, **kwargs: Any) -> None:  # noqa: ANN401
        """Encapsulated info method with automatic UID inclusion."""
        self._log(SeverityLevel.INFO, message, extra_value, **kwargs)

    def success(self, message: str, extra_value: str | None = None, **kwargs: Any) -> None:  # noqa: ANN401
        """Encapsulated success method with automatic UID inclusion."""
        self._log(SeverityLevel.SUCCESS, message, **kwargs, extra_value=extra_value)

    def warning(self, message: str, extra_value: str | None = None, **kwargs: Any) -> None:  # noqa: ANN401
        """Encapsulated warning method with automatic UID inclusion."""
        self._log(SeverityLevel.WARNING, message, **kwargs, extra_value=extra_value)

    def error(self, message: str, extra_value: str | None = None, **kwargs: Any) -> None:  # noqa: ANN401
        """Encapsulated error method with automatic UID inclusion."""
        self._log(SeverityLevel.ERROR, message, **kwargs, extra_value=extra_value)

    def critical(self, message: str, extra_value: str | Exception | None = None, **kwargs: Any) -> None:  # noqa: ANN401
        """Encapsulated critical method with automatic UID inclusion."""
        self._log(SeverityLevel.CRITICAL, message, exception_message=extra_value, extra_value=None, **kwargs)
