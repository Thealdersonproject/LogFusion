# ./yaplogger/decorators.py
# ruff: noqa
"""Decorators to log function and method calls.

This module provides decorators to log function and method calls. The decorators use the `Logger` class from
the `yaplogger` package to log information about the function or method being called, including the arguments and
return values. If an exception occurs, the decorators will log the exception and re-raise it.

Decorators:
    - log_function: Decorator to log function calls.
    - log_method: Decorator to log method calls.

Usage:
    ```python
    from yaplogger.decorators import log_function, log_method


    @log_function()
    def example_function(x: int, y: int) -> int:
        return x + y


    class ExampleClass:
        @log_method()
        def example_method(self, x: int, y: int) -> int:
            return x + y


    # Call the decorated function and method
    result = example_function(3, 4)
    example = ExampleClass()
    result = example.example_method(5, 6)
    ```

Note:
    This module is part of the YapLogger project, which aims to provide a flexible and extensible logging
    framework for logging, monitoring, and observability.
"""

from functools import wraps
from typing import Any, ParamSpec

from yaplogger.config import get_config
from yaplogger.logger import Logger

P = ParamSpec("P")


def log_function(config: dict[str, Any] | None = None) -> Any:
    """Decorator to log function calls.

    Args:
        config (dict, optional): The logging configuration. If not provided, the default configuration will be used.
    """
    config = config or get_config()
    logger = Logger(config)

    def decorator(func) -> Any:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs):
            logger.info(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
            try:
                result = func(*args, **kwargs)
                logger.info(f"{func.__name__} returned {result}")
            except Exception as e:
                logger.exception(f"{func.__name__} raised an exception.", exc_info=e)
                raise
            return result

        return wrapper

    return decorator


def log_method(config: dict[str, Any] | None = None):
    """Decorator to log method calls.

    Args:
        config (dict, optional): The logging configuration. If not provided, the default configuration will be used.
    """
    config = config or get_config()
    logger = Logger(config)

    def decorator(method):
        @wraps(method)
        def wrapper(self, *args: P.args, **kwargs: P.kwargs):
            logger.info(f"Calling {method.__name__} with args: {args} and kwargs: {kwargs}")
            try:
                result = method(self, *args, **kwargs)
                logger.info(f"{method.__name__} returned {result}")
            except Exception as e:
                logger.exception(f"{method.__name__} raised an exception.", exc_info=e)
                raise
            return result

        return wrapper

    return decorator
