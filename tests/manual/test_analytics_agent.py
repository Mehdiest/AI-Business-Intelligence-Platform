"""
Manual Analytics Agent test.
"""

from app.database import SessionLocal

from app.services.ai.vector_store.manager import (
    VectorManager,
)

from app.services.ai.copilot.context_runtime import (
    ExecutionContextFactory,
)

from app.services.ai.copilot.agents.planner import (
    PlannerAgent,
)

from app.services.ai.copilot.executor import (
    ExecutionEngine,
)


def main():

    db = SessionLocal()

    VectorManager.initialize(db)

    planner = PlannerAgent()

    engine = ExecutionEngine()

    context = (
        ExecutionContextFactory.create(
            "Top selling product"
        )
    )

    context.plan = (
        planner.build_plan(
            context.question
        )
    )

    context = engine.execute(
        context
    )

    print()

    print(context.analytics)

    assert (
        context.analytics[
            "document_count"
        ]
        > 0
    )

    assert (
        context.analytics[
            "highest_score"
        ]
        > 0
    )

    assert (
        context.analytics[
            "top_document"
        ]
        is not None
    )

    print()

    print("=" * 60)

    print("SUCCESS")

    print("=" * 60)

    print(
        "Analytics Agent passed."
    )

    db.close()


if __name__ == "__main__":

    main()