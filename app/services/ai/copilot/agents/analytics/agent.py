"""
Enterprise Analytics Agent.
"""

from __future__ import annotations

from app.services.ai.copilot.context_runtime import (
    ExecutionContext,
)

from .base import (
    BaseAnalyticsAgent,
)


class AnalyticsAgent(
    BaseAnalyticsAgent,
):
    """
    Extracts business analytics from
    retrieved semantic context.
    """

    def run(
        self,
        context: ExecutionContext,
    ) -> ExecutionContext:

        documents = []

        if context.retrieved_context:

            documents = (
                context.retrieved_context.documents
            )

        context.analytics = {

            "document_count":
                len(documents),

            "highest_score":
                max(
                    (
                        d.score
                        for d in documents
                    ),
                    default=0.0,
                ),

            "top_document":
                (
                    documents[0].text
                    if documents
                    else None
                ),
        }

        return context