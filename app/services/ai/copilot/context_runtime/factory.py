"""
Execution context factory.
"""

from __future__ import annotations

from .models import (
    ExecutionContext,
)


class ExecutionContextFactory:
    """
    Creates enterprise execution
    contexts.
    """

    @staticmethod
    def create(
        question: str,
    ) -> ExecutionContext:
        """
        Create a fresh runtime context.

        Parameters
        ----------
        question:
            User question.

        Returns
        -------
        ExecutionContext
        """

        return ExecutionContext(
            question=question,
        )