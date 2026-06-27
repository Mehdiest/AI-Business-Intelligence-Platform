"""
Base planner interface.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from .models import ExecutionPlan


class BasePlanner(ABC):
    """
    Abstract planner interface.

    Every planner implementation must
    return an execution plan that can
    later be executed by the orchestration
    engine.
    """

    @abstractmethod
    def build_plan(
        self,
        question: str,
    ) -> ExecutionPlan:
        """
        Build an execution plan.

        Parameters
        ----------
        question:
            User question.

        Returns
        -------
        ExecutionPlan
        """
        ...