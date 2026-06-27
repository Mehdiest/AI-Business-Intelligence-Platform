"""
Enterprise planner agent.
"""

from __future__ import annotations

from .base import BasePlanner
from .models import ExecutionPlan
from .rules import PlannerRules


class PlannerAgent(
    BasePlanner,
):
    """
    Converts a user question into
    an execution plan.

    The planner never executes work.
    It only decides the sequence of
    operations required to answer
    the request.
    """

    def build_plan(
        self,
        question: str,
    ) -> ExecutionPlan:

        steps, reason = (
            PlannerRules.resolve(
                question
            )
        )

        return ExecutionPlan(
            steps=steps,
            reasoning=reason,
        )