"""
Global exception middleware.
"""

from __future__ import annotations

from starlette.middleware.base import (
    BaseHTTPMiddleware,
)
from starlette.responses import (
    JSONResponse,
)

from app.core.logging import (
    get_logger,
)


logger = get_logger(
    "ExceptionMiddleware"
)


class ExceptionMiddleware(
    BaseHTTPMiddleware,
):

    async def dispatch(
        self,
        request,
        call_next,
    ):

        try:

            return await call_next(
                request
            )

        except Exception as exc:

            logger.exception(exc)

            return JSONResponse(
                status_code=500,
                content={
                    "detail":
                    "Internal server error."
                },
            )