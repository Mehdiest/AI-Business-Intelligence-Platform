"""
Agent registry.
"""

from __future__ import annotations

from typing import Callable

from app.services.ai.copilot.agents.planner.models import (
    ExecutionStep,
)

from app.services.ai.copilot.agents.retriever import (
    RetrieverAgent,
)

from app.services.ai.copilot.agents.analytics import (
    AnalyticsAgent,
)


class AgentRegistry:
    """
    Registry for executable agents.
    """

    def __init__(self):

        retriever = RetrieverAgent()

        analytics = AnalyticsAgent()

        self._agents = {

            ExecutionStep.RETRIEVE:
                retriever.run,

            ExecutionStep.ANALYTICS:
                analytics.run,

        }

    def register(
        self,
        step: ExecutionStep,
        handler: Callable,
    ) -> None:

        self._agents[
            step
        ] = handler

    def get(
        self,
        step: ExecutionStep,
    ) -> Callable | None:

        return self._agents.get(
            step
        )