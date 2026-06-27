"""
Base Response Agent.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from app.services.ai.copilot.context_runtime import (
    ExecutionContext,
)

from .models import (
    ResponseContext,
)


class BaseResponseAgent(
    ABC,
):
    """
    Base response interface.
    """

    @abstractmethod
    def run(
        self,
        context: ExecutionContext,
    ) -> ResponseContext:
        ...