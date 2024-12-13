# ruff: noqa
"""Tests YapLogger basic usage."""

from typing import Any

from yaplogger.config import get_config, set_config
from yaplogger.logger import Logger


def main() -> None:
    """Main function to demonstrate the basic usage of the Logger."""
    # Set the configuration
    config: dict[str, Any] = {"log_level": "DEBUG", "dev_mode": False, "handlers": {"loguru": {}}}
    set_config(config)

    # Get the configuration
    config = get_config()
    logger = Logger(config)

    # Example log messages
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")

    try:
        # Simulate an exception
        msg = "An example exception"
        raise ValueError(msg)  # noqa: TRY301
    except Exception as e:
        logger.exception("An exception occurred", exc_info=e)
        logger.exception(f"An exception occurred:", exc_info=e)  # pyright: ignore [reportCallIssue]
        logger.info("Let's move on.")


if __name__ == "__main__":
    main()
