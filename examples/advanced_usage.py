# ./examples/advanced_usage.py
"""Tests YapLogger advanced usage.

This module demonstrates the advanced usage of the YapLogger logging framework.
It includes examples of setting and getting configuration, using logging decorators,
and handling exceptions with the Logger class.

Functions:
    - example_function: A function decorated with `log_function` to demonstrate logging.
    - main: The main function that demonstrates the advanced usage of the Logger.

Classes:
    - ExampleClass: A class with a method decorated with `log_method` to demonstrate logging.

Usage:
    To run the advanced usage examples, execute the `main` function.

Example:
    ```python
    if __name__ == "__main__":
        main()
    ```

Note:
    This module is part of the YapLogger project, which aims to provide a flexible
    and extensible logging framework for logging, monitoring, and observability.
"""

from typing import Any

from yaplogger import Logger, get_config, set_config
from yaplogger.decorators import log_function, log_method

# Set the configuration
config: dict[str, Any] = {"log_level": "DEBUG", "dev_mode": False, "handlers": {"loguru": {}}}
set_config(config)

# Get the configuration
config = get_config()
logger = Logger(config)


@log_function(config)
def example_function(x: int, y: int) -> int:
    """Example function to demonstrate logging."""
    return x + y


class ExampleClass:
    """Example class to demonstrate logging."""

    @log_method(config)
    def example_method(self, x: int, y: int) -> int:
        """Example method to demonstrate logging."""
        return x + y


def main() -> None:
    """Main function to demonstrate the advanced usage of the Logger."""
    # Example function call
    result = example_function(3, 4)
    logger.info(f"Result of example_function: {result}")

    # Example method call
    example = ExampleClass()
    result = example.example_method(5, 6)
    logger.info(f"Result of example_method: {result}")

    try:
        # Simulate an exception in a function
        @log_function(config)
        def failing_function():  # noqa: ANN202
            raise ValueError("An example exception in a function")  # noqa: EM101, TRY003, TRY301

        failing_function()
    except Exception as e:
        logger.exception("An exception occurred in a function", exc_info=e)


if __name__ == "__main__":
    main()
