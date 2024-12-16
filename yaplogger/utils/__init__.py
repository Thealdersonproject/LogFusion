# whoami::./yaplogger/utils/__init__.py
"""Yaplogger Utils."""

from yaplogger.utils.decorators import singleton
from yaplogger.utils.enums import LogLevel, SeverityLevel

__all__ = ["LogLevel", "SeverityLevel", "singleton"]
