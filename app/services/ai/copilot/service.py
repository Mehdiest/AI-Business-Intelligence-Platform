"""
Enterprise Copilot Service.
"""

from __future__ import annotations

from app.services.ai.copilot.engine import (
    CopilotEngine,
)

from app.services.ai.copilot.models import (
    CopilotRequest,
    CopilotResponse,
)


class CopilotService:
    """
    Enterprise AI Copilot.
    """

    def __init__(self):

        self.engine = CopilotEngine()

    def ask(
        self,
        request: CopilotRequest,
    ) -> CopilotResponse:

        return self.engine.process(
            request
        )