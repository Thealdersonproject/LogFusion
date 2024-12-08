# ruff: noqa
"""Decorators to log function and method calls."""

from functools import wraps
from typing import Any, ParamSpec

from logfusion.config import get_config
from logfusion.logger import Logger

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
