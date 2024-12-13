# ./yaplogger/__init__.py
"""This is the __init__.py file for the YapLogger package.

The YapLogger package provides a flexible and extensible logging framework for logging, monitoring, and observability.
This package includes configuration management, utility functions, decorators for logging, and the main Logger class.

Modules:
    - config: Contains functions and default configurations for the YapLogger package.
    - decorators: Contains decorators for logging functions and methods.
    - logger: Contains the main Logger class for logging messages.

Functions and Classes:
    - Logger: The main class for logging messages.
    - default_config: The default configuration for the YapLogger package.
    - get_config: Function to retrieve the current configuration.
    - set_config: Function to set the configuration.
    - log_function: Decorator for logging function calls.
    - log_method: Decorator for logging method calls.

Usage:
    To use the YapLogger package, you can import the Logger class and other utilities as needed.

Example:
    ```python
    from yaplogger import Logger, default_config, set_config, log_function, log_method

    # Set the configuration
    config = default_config
    set_config(config)

    # Create a logger instance
    logger = Logger(config)

    # Use the logger
    logger.info("This is an info message.")


    # Decorate a function
    @log_function(config)
    def example_function(x: int, y: int) -> int:
        return x + y


    # Decorate a method
    class ExampleClass:
        @log_method(config)
        def example_method(self, x: int, y: int) -> int:
            return x + y
    ```
"""

from .config import default_config, get_config, set_config
from .decorators import log_function, log_method
from .logger import Logger

__all__ = ["Logger", "default_config", "get_config", "log_function", "log_method", "set_config"]
