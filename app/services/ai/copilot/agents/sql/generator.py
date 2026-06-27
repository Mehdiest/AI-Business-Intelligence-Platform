"""
Enterprise SQL Generator.
"""

from __future__ import annotations

from .models import (
    SQLGenerationResult,
    SQLPlan,
)


class SQLGenerator:
    """
    Enterprise SQL Generator.

    Current version:
        Rule-based

    Future:
        LLM + Schema-aware generation.
    """

    def generate(
        self,
        question: str,
        plan: SQLPlan,
    ) -> SQLGenerationResult:

        q = question.lower()

        # ---------------------------------------------------
        # Top selling product
        # ---------------------------------------------------

        if (
            "top" in q
            and "product" in q
        ):

            return SQLGenerationResult(

                sql="""
SELECT
    p.product_name,
    SUM(f.amount) AS revenue
FROM fact_sales AS f
JOIN dim_product AS p
    ON f.product_id = p.id
GROUP BY p.product_name
ORDER BY revenue DESC
LIMIT 1
""".strip()

            )

        # ---------------------------------------------------
        # Total Sales
        # ---------------------------------------------------

        if (
            "total sales" in q
            or "revenue" in q
        ):

            return SQLGenerationResult(

                sql="""
SELECT
SUM(amount) AS total_sales
FROM fact_sales
""".strip()

            )

        # ---------------------------------------------------
        # Average Sales
        # ---------------------------------------------------

        if "average" in q:

            return SQLGenerationResult(

                sql="""
SELECT
AVG(amount) AS average_sales
FROM fact_sales
""".strip()

            )

        # ---------------------------------------------------
        # Default
        # ---------------------------------------------------

        return SQLGenerationResult(

            sql="""
SELECT
*
FROM fact_sales
LIMIT 10
""".strip()

        )