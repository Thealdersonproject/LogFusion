# whoami::./yaplogger/config.py
"""This module is to set the YapLogger configuration parameters, by using the Config class."""

import time
import uuid
from typing import Any, ClassVar

from loguru import logger

from constants import Constants


class Config:
    """Handles the configuration settings for the application.

    The Config class is responsible for managing configuration settings that define the
    application's behavior. It provides methods to configure, retrieve, and manipulate
    configuration values, while also ensuring that specific defaults are set when no
    custom configuration is supplied. The class supports extensibility by allowing
    unrecognized keys to be added to an extras section. Furthermore, it generates and
    manages a unique process identifier (UID) to aid in identifying application
    instances.
    """

    _configuration: ClassVar[dict[str, Any]] = {
        Constants.PROCESS_UID_KEY: Constants.PROCESS_UID_DEFAULT_VALUE,
        Constants.PROCESS_NAME_KEY: Constants.PROCESS_NAME_DEFAULT_VALUE,
        Constants.PROCESS_DESCRIPTION_KEY: Constants.DESCRIPTION_DEFAULT_VALUE,
        Constants.PROCESS_EXTRAS_KEY: [],
    }

    def configure(self, *, parameters: dict[str, Any] | None) -> dict[str, Any]:
        """Configures the application with given settings.

        This static method modifies the application's internal configuration based on the provided data.
        If no configuration is provided, default values will be used. Unrecognized keys will be collected into
        an extras section for further processing.

        Args:
            parameters (dict[str, Any] | None): A dictionary of configuration settings where keys
            represent configuration names, and the values are their corresponding settings.
            If None, default configuration will be applied.
        """
        logger.debug(f"Config keys: {parameters.keys() if parameters else []}")

        if not parameters:
            logger.debug("No information provided for configuration.")
            logger.debug("Default values will be applied.")

        else:
            for k, v in parameters.items():
                clean_key: str = str(k).lower().strip()
                logger.debug(f"Validating key: {clean_key}.")
                if clean_key in self._configuration:
                    Config._configuration[clean_key] = v
                    logger.debug(f"Key <{clean_key}> set with value: <{v}>")
                else:
                    logger.debug(f"Key '{k}' not found in default configuration, will be added to extras.")
                    Config._configuration[Constants.PROCESS_EXTRAS_KEY].append({clean_key: v})

        self.__set_process_id()
        logger.debug(f"Configuration values: {self.parameters}")

        return self.parameters

    @classmethod
    def get_process_id(cls) -> str:
        """Gets the process identifier for the current class instance.

        This method retrieves a unique process ID from the configuration stored within
        the class. If the process ID key is not found, it defaults to the specified
        default value.

        @return: The unique process identifier as a string.
        """
        return cls._configuration.get(Constants.PROCESS_UID_KEY, Constants.PROCESS_UID_DEFAULT_VALUE)

    def __set_process_id(self) -> None:
        """Sets a unique process identifier (UID) for the application if not already set.

        This static utility method attempts to generate a new unique process identifier
        based on the current Unix epoch timestamp, as well as certain application
        configuration parameters, such as the process name and description. If a
        process UID is already defined and meets the required conditions, the operation
        is skipped, and debug messages are logged to indicate this. Otherwise, the
        newly generated UID is stored in the application configuration.

        The generated UID uses the Version 5 UUID standard based on specific name-based
        inputs to ensure consistency and uniqueness.

        Attributes:
        ----------
        None

        Parameters:
        ----------
        None
        """
        config = self._configuration
        if (
            Constants.PROCESS_UID_KEY in config
            and config[Constants.PROCESS_UID_KEY] is not None
            and len(config[Constants.PROCESS_UID_KEY]) > 0
            and config[Constants.PROCESS_UID_KEY] != Constants.PROCESS_UID_DEFAULT_VALUE
        ):
            logger.debug(f"Process has already set the uid to: {config[Constants.PROCESS_UID_KEY]}")
            logger.debug("Skipping to generate new process uid.")
            return

        unix_epoch_timestamp: int = int(time.time())
        process_name = self.parameters.get(Constants.PROCESS_NAME_KEY, Constants.PROCESS_UID_DEFAULT_VALUE)
        process_description = self.parameters.get(
            Constants.PROCESS_DESCRIPTION_KEY, Constants.DESCRIPTION_DEFAULT_VALUE
        )

        uid = uuid.uuid5(uuid.NAMESPACE_DNS, str(unix_epoch_timestamp) + process_name + process_description)
        self._configuration[Constants.PROCESS_UID_KEY] = str(uid)

    @property
    def parameters(self) -> dict[str, Any]:
        """Retrieve the application's configuration details.

        This method is responsible for fetching and returning the configuration settings
        stored in the internal configuration dictionary of the `Config` class. The
        configuration encapsulates various settings used throughout the application.

        Returns:
            dict[str, Any]: A dictionary containing the configuration data.
        """
        return self._configuration
