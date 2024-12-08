"""Tests LogFusion advanced usage."""

from typing import Any

from logfusion.config import get_config, set_config
from logfusion.decorators import log_function, log_method
from logfusion.logger import Logger

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
