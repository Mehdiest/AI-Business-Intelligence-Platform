"""
Manual Multi-Agent Pipeline.
"""

from app.services.ai.vector_store.manager import (
    VectorManager,
)

from app.database import (
    SessionLocal,
)

from app.services.ai.copilot.service import (
    CopilotService,
)

from app.services.ai.copilot.models import (
    CopilotRequest,
)


def main():

    db = SessionLocal()

    VectorManager.initialize(
        db
    )

    service = CopilotService()

    result = service.ask(

        CopilotRequest(

            question="Top selling product"

        )

    )

    print()

    print(result.model_dump())

    assert result.answer is not None

    assert result.confidence > 0

    print()

    print("=" * 60)

    print("SUCCESS")

    print("=" * 60)

    print("Multi-Agent Pipeline passed.")


if __name__ == "__main__":

    main()