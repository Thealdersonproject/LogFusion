"""Load the configuration from pyproject.toml."""

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
