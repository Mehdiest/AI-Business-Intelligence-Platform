"""
Dashboard API endpoints.

Provides analytics and KPI data for
BI dashboards and frontend consumers.
"""

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.dashboard import (
    KPIResponse,
    ProductSalesResponse,
    RegionSalesResponse,
    MonthlySalesResponse,
)
from app.services.analytics.kpi import KPIService
from app.services.analytics.stats import AnalyticsService

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.get(
    "/kpis",
    response_model=KPIResponse,
)
def get_kpis(
    db: Session = Depends(get_db),
):
    """
    Return top-level KPI metrics.
    """

    service = KPIService(db)

    return service.get_kpis()


@router.get(
    "/sales-by-region",
    response_model=list[RegionSalesResponse],
)
def sales_by_region(
    db: Session = Depends(get_db),
):
    """
    Return sales aggregated by region.
    """

    service = AnalyticsService(db)

    return service.sales_by_region()


@router.get(
    "/top-products",
    response_model=list[ProductSalesResponse],
)
def top_products(
    db: Session = Depends(get_db),
):
    """
    Return top-selling products.
    """

    service = AnalyticsService(db)

    return service.top_products()


@router.get(
    "/monthly-sales",
    response_model=list[MonthlySalesResponse],
)
def monthly_sales(
    db: Session = Depends(get_db),
):
    """
    Return sales trend over time.
    """

    service = AnalyticsService(db)

    return service.monthly_sales()