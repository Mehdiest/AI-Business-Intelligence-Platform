"""
Manual test for Retriever Agent.
"""

from __future__ import annotations

from app.database import SessionLocal

from app.services.ai.vector_store.manager import (
    VectorManager,
)

from app.services.ai.copilot.agents.retriever import (
    RetrieverAgent,
)


def print_separator(
    title: str,
) -> None:

    print()

    print("=" * 60)

    print(title)

    print("=" * 60)


def main() -> None:

    db = SessionLocal()

    print_separator(
        "STEP 1 - Initialize Vector Store"
    )

    VectorManager.initialize(db)

    print(
        "Indexed Documents:",
        VectorManager.indexed_documents(),
    )

    print_separator(
        "STEP 2 - Retriever Agent"
    )

    agent = RetrieverAgent()

    context = {
        "question": "Top selling product",
    }

    result = agent.run(
        context
    )

    assert (
        "retrieved_context"
        in result
    )

    print(
        result[
            "retrieved_context"
        ].model_dump()
    )

    print()

    print("=" * 60)

    print("SUCCESS")

    print("=" * 60)

    print(
        "Retriever Agent passed all manual tests."
    )

    db.close()


if __name__ == "__main__":

    main()