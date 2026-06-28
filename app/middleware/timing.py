"""
Request timing middleware.
"""

from __future__ import annotations

import time

from starlette.middleware.base import BaseHTTPMiddleware


class TimingMiddleware(
    BaseHTTPMiddleware,
):
    """
    Measures request execution time.
    """

    async def dispatch(
        self,
        request,
        call_next,
    ):

        start = time.perf_counter()

        response = await call_next(
            request
        )

        duration = (
            time.perf_counter()
            - start
        )

        response.headers[
            "X-Process-Time"
        ] = (
            f"{duration:.4f}"
        )

        return response