"""
AI Insight generation service.

Creates business insights from warehouse data.
"""

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.warehouse import (
    FactSales,
    DimRegion,
    DimProduct,
)


class InsightService:
    """
    Business intelligence insight engine.
    """

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def generate_insight(self) -> dict:
        """
        Generate a primary business insight.
        """

        total_sales = float(
            self.db.query(
                func.sum(FactSales.amount)
            )
            .scalar()
            or 0
        )

        top_region = (
            self.db.query(
                DimRegion.region_name,
                func.sum(FactSales.amount).label(
                    "sales"
                ),
            )
            .join(
                FactSales,
                FactSales.region_id == DimRegion.id,
            )
            .group_by(
                DimRegion.region_name
            )
            .order_by(
                func.sum(
                    FactSales.amount
                ).desc()
            )
            .first()
        )

        if not top_region:
            return {
                "insight": (
                    "No sales data available."
                )
            }

        region_name = top_region[0]
        region_sales = float(top_region[1])

        contribution = (
            (region_sales / total_sales) * 100
            if total_sales > 0
            else 0
        )

        return {
            "insight": (
                f"{region_name} region generated "
                f"{contribution:.1f}% of total sales "
                f"and is currently the top-performing region."
            )
        }

    def executive_summary(self) -> dict:
        """
        Generate executive summary.
        """

        total_sales = (
            self.db.query(
                func.sum(FactSales.amount)
            )
            .scalar()
            or 0
        )

        total_orders = (
            self.db.query(
                FactSales.id
            ).count()
        )

        return {
            "summary": (
                f"The business generated "
                f"{total_sales:,.0f} in revenue "
                f"across {total_orders} sales transactions."
            )
        }

    def sales_narrative(self) -> dict:
        """
        Generate sales narrative.
        """

        top_product = (
            self.db.query(
                DimProduct.product_name,
                func.sum(FactSales.amount).label(
                    "sales"
                ),
            )
            .join(
                FactSales,
                FactSales.product_id == DimProduct.id,
            )
            .group_by(
                DimProduct.product_name
            )
            .order_by(
                func.sum(
                    FactSales.amount
                ).desc()
            )
            .first()
        )

        if not top_product:
            return {
                "narrative": (
                    "No sales activity detected."
                )
            }

        return {
            "narrative": (
                f"{top_product[0]} is currently "
                f"the strongest product in the portfolio."
            )
        }