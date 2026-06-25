"""
AI response schemas.
"""

from pydantic import BaseModel


class InsightResponse(BaseModel):
    """
    Business insight response.
    """

    insight: str


class ExecutiveSummaryAIResponse(BaseModel):
    """
    Executive AI summary.
    """

    summary: str


class SalesNarrativeResponse(BaseModel):
    """
    Sales narrative response.
    """

    narrative: str