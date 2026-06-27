"""
Enterprise Multi-Agent Copilot Engine.
"""

from __future__ import annotations

from app.services.ai.copilot.models import (
    CopilotRequest,
    CopilotResponse,
    SourceReference,
)

from app.services.ai.copilot.context import (
    ContextBuilder,
)

from app.services.ai.copilot.prompt import (
    PromptBuilder,
)

from app.services.ai.copilot.intent import (
    RuleBasedIntentClassifier,
)

from app.services.ai.copilot.context_runtime import (
    ExecutionContext,
)

from app.services.ai.copilot.agents.analytics import (
    AnalyticsAgent,
)

from app.services.ai.copilot.agents.retriever import (
    RetrieverAgent,
)

from app.services.ai.copilot.agents.response import (
    ResponseAgent,
)

from app.services.ai.copilot.agents.sql import (
    SQLAgent,
)

from app.services.ai.llm import (
    LLMFactory,
)


class CopilotEngine:
    """
    Enterprise Multi-Agent Engine.
    """

    def __init__(self):

        self.intent = RuleBasedIntentClassifier()

        self.context_builder = ContextBuilder()

        self.retriever = RetrieverAgent()

        self.analytics = AnalyticsAgent()

        self.sql = SQLAgent()

        self.response = ResponseAgent()

        self.prompt_builder = PromptBuilder()

        self.llm = LLMFactory.create()

    def process(
        self,
        request: CopilotRequest,
    ) -> CopilotResponse:

        intent = self.intent.classify(
            request.question
        )

        retrieval = self.context_builder.build(
            request.question
        )

        runtime = ExecutionContext(
            question=request.question
        )

        runtime.retrieved_context = retrieval

        runtime = self.retriever.run(
            runtime
        )

        runtime = self.analytics.run(
            runtime
        )

        runtime = self.sql.run(
            runtime
        )

        response_context = self.response.run(
            runtime
        )

        prompt = self.prompt_builder.build(

            question=response_context.question,

            context=retrieval,

        )

        answer = self.llm.generate(
            prompt
        )

        sources = []

        for index, text in enumerate(

            response_context.citations,

            start=1,

        ):

            sources.append(

                SourceReference(

                    id=str(index),

                    text=text,

                    score=1.0,

                )

            )

        return CopilotResponse(

            answer=answer,

            confidence=intent.confidence,

            sources=sources,

        )