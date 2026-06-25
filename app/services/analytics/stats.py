"""
Analytics aggregation service.

Provides aggregated datasets for
dashboards, charts, and BI tools.
"""

from __future__ import annotations

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.warehouse import (
    DimDate,
    DimProduct,
    DimRegion,
    FactSales,
)


class AnalyticsService:
    """
    Dashboard analytics service.
    """

    def __init__(self, db: Session):
        self.db = db

    def sales_by_region(self) -> list[dict]:

        results = (
            self.db.query(
                DimRegion.region_name,
                func.sum(
                    FactSales.amount
                ).label("sales"),
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
            .all()
        )

        return [
            {
                "region": region,
                "sales": float(sales),
            }
            for region, sales in results
        ]

    def top_products(
        self,
        limit: int = 10,
    ) -> list[dict]:

        results = (
            self.db.query(
                DimProduct.product_name,
                func.sum(
                    FactSales.amount
                ).label("sales"),
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
            .limit(limit)
            .all()
        )

        return [
            {
                "product": product,
                "sales": float(sales),
            }
            for product, sales in results
        ]

    def monthly_sales(self) -> list[dict]:

        results = (
            self.db.query(
                DimDate.full_date,
                func.sum(
                    FactSales.amount
                ).label("sales"),
            )
            .join(
                FactSales,
                FactSales.date_id == DimDate.id,
            )
            .group_by(
                DimDate.full_date
            )
            .order_by(
                DimDate.full_date
            )
            .all()
        )

        return [
            {
                "month": str(date),
                "sales": float(sales),
            }
            for date, sales in results
        ]