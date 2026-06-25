"""
KPI calculation service.

Provides warehouse-level business metrics
used by dashboards and BI consumers.
"""

from __future__ import annotations

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.warehouse import (
    DimProduct,
    DimRegion,
    FactSales,
)


class KPIService:
    """
    Business KPI calculations.
    """

    def __init__(self, db: Session):
        self.db = db

    def get_kpis(self) -> dict:
        """
        Calculate top-level KPIs.
        """

        total_sales = (
            self.db.query(
                func.coalesce(
                    func.sum(FactSales.amount),
                    0,
                )
            )
            .scalar()
        )

        total_orders = (
            self.db.query(
                FactSales.id
            )
            .count()
        )

        average_order_value = (
            float(total_sales) / total_orders
            if total_orders
            else 0
        )

        top_region = self._get_top_region()

        top_product = self._get_top_product()

        return {
            "total_sales": round(
                float(total_sales),
                2,
            ),
            "total_orders": total_orders,
            "average_order_value": round(
                average_order_value,
                2,
            ),
            "top_region": top_region,
            "top_product": top_product,
        }

    def _get_top_region(self) -> str:

        result = (
            self.db.query(
                DimRegion.region_name,
                func.sum(
                    FactSales.amount
                ).label("sales"),
            )
            .join(
                FactSales,
                FactSales.region_id
                == DimRegion.id,
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

        return result[0] if result else "N/A"

    def _get_top_product(self) -> str:

        result = (
            self.db.query(
                DimProduct.product_name,
                func.sum(
                    FactSales.amount
                ).label("sales"),
            )
            .join(
                FactSales,
                FactSales.product_id
                == DimProduct.id,
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

        return result[0] if result else "N/A"