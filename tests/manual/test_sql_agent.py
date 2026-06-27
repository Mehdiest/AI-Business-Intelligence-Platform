"""
Manual SQL Agent test.
"""

from app.services.ai.copilot.agents.sql import (
    SQLAgent,
)

from app.services.ai.copilot.context_runtime import (
    ExecutionContext,
)


def main():

    agent = SQLAgent()

    context = ExecutionContext(

        question="Top selling product"

    )

    result = agent.run(

        context

    )

    print()

    print(result.sql_result)

    assert result.sql_result is not None

    assert "rows" in result.sql_result

    print()

    print("=" * 60)

    print("SUCCESS")

    print("=" * 60)

    print(

        "SQL Agent passed."

    )


if __name__ == "__main__":

    main()