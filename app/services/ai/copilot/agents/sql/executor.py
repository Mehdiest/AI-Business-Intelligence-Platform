"""
Enterprise SQL Executor.
"""

from __future__ import annotations

import time

from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database import SessionLocal

from .models import (
    SQLExecutionResult,
)


class SQLExecutor:
    """
    Executes SQL safely.
    """

    def execute(
        self,
        sql: str,
    ) -> SQLExecutionResult:

        start = time.perf_counter()

        session: Session = SessionLocal()

        try:

            result = session.execute(
                text(sql)
            )

            rows = [

                dict(row._mapping)

                for row in result

            ]

            elapsed = (

                time.perf_counter()

                - start

            ) * 1000

            return SQLExecutionResult(

                sql=sql,

                rows=rows,

                row_count=len(rows),

                execution_time_ms=round(
                    elapsed,
                    2,
                ),

            )

        finally:

            session.close()