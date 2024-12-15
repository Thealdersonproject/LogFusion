# ruff: noqa
# ./examples/basic_usage.py
"""Tests YapLogger basic usage."""

from typing import Any

from yaplogger.config import set_config
from yaplogger.logger import Logger


def main() -> None:
    """Main function to demonstrate the basic usage of the Logger."""
    # Set the configuration
    config: dict[str, Any] = {}  # Placeholder for future configurations
    set_config(config=config)
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
        # raise ValueError(msg)  # noqa: TRY301
    except Exception as e:
        logger.exception("An exception occurred", e)
        logger.exception("An exception occurred:", e)  # pyright: ignore [reportCallIssue]
    else:
        logger.info("No error occurried.")


if __name__ == "__main__":
    main()
