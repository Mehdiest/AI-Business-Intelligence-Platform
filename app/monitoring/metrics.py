"""
Application metrics.
"""

from __future__ import annotations

import platform
import time


class MetricsCollector:
    """
    Simple application metrics.
    """

    started_at = time.time()

    @classmethod
    def collect(cls):

        uptime = round(
            time.time() - cls.started_at,
            2,
        )

        return {

            "python": platform.python_version(),

            "platform": platform.system(),

            "uptime_seconds": uptime,

            "environment": "development",

            "version": "0.7.5",

        }