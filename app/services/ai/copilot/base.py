"""
Shared base classes for enterprise AI services.
"""

from __future__ import annotations

from app.core.logging import get_logger


class BaseService:
    """
    Base service providing enterprise logger.
    """

    def __init__(self) -> None:

        self.logger = get_logger(
            self.__class__.__name__
        )