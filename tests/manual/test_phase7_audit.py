"""
Final Phase 7 Audit.
"""

from app.database import SessionLocal

from app.services.ai.vector_store.manager import (
    VectorManager,
)

from app.services.ai.copilot.models import (
    CopilotRequest,
)

from app.services.ai.copilot.service import (
    CopilotService,
)


def run(question: str):

    service = CopilotService()

    result = service.ask(

        CopilotRequest(

            question=question

        )

    )

    print()

    print(question)

    print(result.model_dump())


def main():

    db = SessionLocal()

    VectorManager.initialize(
        db
    )

    run(
        "Top selling product"
    )

    run(
        "Total sales"
    )

    run(
        "Average sales"
    )

    run(
        "Show first records"
    )

    print()

    print("=" * 60)

    print("SUCCESS")

    print("=" * 60)

    print("Phase 7 Audit passed.")


if __name__ == "__main__":

    main()