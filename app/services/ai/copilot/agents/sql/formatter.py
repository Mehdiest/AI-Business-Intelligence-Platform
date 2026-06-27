"""
Enterprise SQL Result Formatter.
"""

from __future__ import annotations

from .models import (
    SQLExecutionResult,
)


class SQLFormatter:
    """
    Formats SQL results.
    """

    def format(
        self,
        result: SQLExecutionResult,
    ) -> dict:

        return {

            "row_count": result.row_count,

            "execution_time_ms": result.execution_time_ms,

            "rows": result.rows,

        }