"""
Request ID middleware.
"""

from __future__ import annotations

import uuid

from starlette.middleware.base import BaseHTTPMiddleware


class RequestIDMiddleware(
    BaseHTTPMiddleware,
):
    """
    Adds a unique request ID to every request.
    """

    async def dispatch(
        self,
        request,
        call_next,
    ):

        request_id = str(
            uuid.uuid4()
        )

        request.state.request_id = (
            request_id
        )

        response = await call_next(
            request
        )

        response.headers[
            "X-Request-ID"
        ] = request_id

        return response