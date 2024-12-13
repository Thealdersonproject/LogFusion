# ./yaplogger/config.py
"""Load the configuration from pyproject.toml.

This module provides functions to load, set, and get the logging configuration for the YapLogger project.
The configuration is stored in a global variable and can be modified using the `set_config` function. The `get_config`
function retrieves the current configuration, taking into account any environment variables that might
override the default settings.

Functions:
    - set_config: Sets the logging configuration.
    - get_config: Retrieves the logging configuration.

Usage:
    ```python
    from yaplogger.config import set_config, get_config

    # Set a new configuration
    new_config = {"log_level": "INFO", "dev_mode": True, "handlers": {"loguru": {}}}
    set_config(new_config)

    # Get the current configuration
    current_config = get_config()
    print(current_config)
    ```
"""

import os
from typing import Any

# Default configuration
default_config: dict[str, Any] = {"log_level": "DEBUG", "dev_mode": False, "handlers": {"loguru": {}}}


def set_config(config: dict[str, Any]) -> None:
    """Set the logging configuration.

    Args:
        config (Dict[str, Any]): The logging configuration.
    """
    global default_config  # noqa: PLW0603
    default_config = config


def get_config() -> dict[str, Any]:
    """Get the logging configuration.

    Returns:
        Dict[str, Any]: The logging configuration.
    """
    # Check for dev_mode environment variable
    default_config["dev_mode"] = os.getenv("dev_mode", "0") == "1"  # noqa: SIM112
    return default_config
