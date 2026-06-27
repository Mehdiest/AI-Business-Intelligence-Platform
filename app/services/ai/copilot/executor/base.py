"""
Base execution engine.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from app.services.ai.copilot.agents.planner.models import (
    ExecutionPlan,
)


class BaseExecutor(
    ABC,
):
    """
    Base execution engine.
    """

    @abstractmethod
    def execute(
        self,
        plan: ExecutionPlan,
        context: dict,
    ) -> dict:
        """
        Execute an execution plan.
        """
        ...