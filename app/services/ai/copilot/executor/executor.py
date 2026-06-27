"""
Enterprise execution engine.
"""

from __future__ import annotations

from app.services.ai.copilot.context_runtime import (
    ExecutionContext,
)

from app.services.ai.copilot.executor.base import (
    BaseExecutor,
)

from app.services.ai.copilot.executor.registry import (
    AgentRegistry,
)


class ExecutionEngine(
    BaseExecutor,
):
    """
    Executes an execution plan.
    """

    def __init__(self):

        self.registry = (
            AgentRegistry()
        )

    def execute(
        self,
        context: ExecutionContext,
    ) -> ExecutionContext:

        if context.plan is None:
            return context

        for step in context.plan.steps:

            handler = (
                self.registry.get(
                    step
                )
            )

            if handler:

                context = handler(
                    context
                )

        return context