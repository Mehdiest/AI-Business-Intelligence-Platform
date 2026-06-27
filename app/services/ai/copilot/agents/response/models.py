"""
Enterprise Response models.
"""

from __future__ import annotations

from pydantic import BaseModel
from pydantic import Field


class ResponseContext(
    BaseModel,
):
    """
    Final response context.

    Passed to Prompt Builder.
    """

    question: str

    retrieved_context: list[str] = Field(
        default_factory=list,
    )

    sql_result: dict | None = None

    analytics: dict | None = None

    citations: list[str] = Field(
        default_factory=list,
    )

    confidence: float = 1.0