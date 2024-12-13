# ./yaplogger/handlers/__init__.py
"""This module initializes the handlers package, which contains various logging handlers for the YapLogger project.

The handlers package provides a base handler class (`BaseHandler`) that can be extended
to create custom logging handlers. This package is designed to be flexible and extensible,
allowing developers to easily add new logging handlers as needed.

Modules:
    - base_handler: Contains the BaseHandler class, which serves as the foundation for all custom logging handlers.

Classes:
    - BaseHandler: The base class for all logging handlers.
    - LoguruHandler: A logging handler that uses Loguru for logging.


Usage:
    To create a custom logging handler, subclass the BaseHandler class and override its methods as needed.

Example:
    ```python
    from handlers.base_handler import BaseHandler


    class CustomHandler(BaseHandler):
        def handle(self, record):
            # Custom handling logic here
            pass
    ```

Note:
    This module is part of the YapLogger project, which aims to provide a flexible and extensible logging framework for
    logging, monitoring, and observability.
"""

from .base_handler import BaseHandler
from .loguru_handler import LoguruHandler

__all__ = ["BaseHandler", "LoguruHandler"]
