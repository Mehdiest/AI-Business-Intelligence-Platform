"""
Planner Agent.
"""

from __future__ import annotations

from app.services.ai.copilot.base import BaseService

from .models import (
    PlannerOutput,
)


class PlannerAgent(BaseService):
    """
    Enterprise Planner Agent.
    """

    def __init__(self):

        super().__init__()

    def execute(
        self,
        question: str,
    ) -> PlannerOutput:

        self.logger.info(
            "Planner started."
        )

        output = PlannerOutput(
            execution_mode="semantic_search",
            confidence=0.95,
        )

        self.logger.info(
            "Planner completed."
        )

        return output