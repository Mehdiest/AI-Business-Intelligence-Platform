"""
Health checking.
"""

from __future__ import annotations

from sqlalchemy import text

from app.database import engine

from .metrics import MetricsCollector


class HealthChecker:

    @staticmethod
    def database():

        try:

            with engine.connect() as conn:

                conn.execute(
                    text("SELECT 1")
                )

            return True

        except Exception:

            return False

    @classmethod
    def status(cls):

        db = cls.database()

        return {

            "status": (
                "healthy"
                if db
                else "unhealthy"
            ),

            "database": db,

            "metrics": (
                MetricsCollector.collect()
            ),

        }