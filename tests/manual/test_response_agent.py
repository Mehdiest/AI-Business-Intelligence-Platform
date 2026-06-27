"""
Manual Response Agent test.
"""

from app.services.ai.copilot.agents.response import (
    ResponseAgent,
)

from app.services.ai.copilot.context.models import (
    ContextDocument,
    RetrievalContext,
)

from app.services.ai.copilot.context_runtime import (
    ExecutionContext,
)


def main():

    context = ExecutionContext(

        question="Top selling product"

    )

    context.retrieved_context = RetrievalContext(

        documents=[

            ContextDocument(

                text="Laptop is the best-selling product.",

                score=0.98,

            )

        ]

    )

    context.analytics = {

        "summary": "analytics ok"

    }

    context.sql_result = {

        "rows": [

            {

                "product_name": "Laptop",

                "revenue": 4500,

            }

        ]

    }

    agent = ResponseAgent()

    result = agent.run(

        context

    )

    print()

    print(result.model_dump())

    assert result.question == "Top selling product"

    assert len(result.retrieved_context) == 1

    assert result.sql_result is not None

    assert result.analytics is not None

    print()

    print("=" * 60)

    print("SUCCESS")

    print("=" * 60)

    print("Response Agent passed.")


if __name__ == "__main__":

    main()