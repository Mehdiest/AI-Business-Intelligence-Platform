"""
Enterprise SQL planner.
"""

from __future__ import annotations

from .models import (
    SQLPlan,
)


class SQLPlanner:
    """
    Determines whether SQL
    execution is required.
    """

    def build_plan(
        self,
        question: str,
    ) -> SQLPlan:

        q = question.lower()

        sql_keywords = (

            "sales",

            "revenue",

            "product",

            "customer",

            "order",

            "region",

            "month",

            "year",

            "top",

            "average",

            "sum",

            "count",

            "total",

        )

        requires_sql = any(

            keyword in q

            for keyword in sql_keywords

        )

        return SQLPlan(

            requires_sql=requires_sql,

            target_table="sales",

            operation="analytics",

            explanation=(

                "Business analytics query"

                if requires_sql

                else

                "No SQL required"

            ),

        )