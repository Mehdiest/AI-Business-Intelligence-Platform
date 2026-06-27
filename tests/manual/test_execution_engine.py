"""
Manual test for the Execution Engine.
"""

from __future__ import annotations

from app.services.ai.copilot.agents.planner import (
    PlannerAgent,
)

from app.services.ai.copilot.executor import (
    ExecutionEngine,
)


def print_separator(
    title: str,
) -> None:

    print()

    print("=" * 60)

    print(title)

    print("=" * 60)


def main() -> None:

    planner = PlannerAgent()

    executor = ExecutionEngine()

    # --------------------------------------------------

    print_separator(
        "STEP 1 - Planner"
    )

    plan = planner.build_plan(
        "Top selling products"
    )

    print(
        plan.model_dump()
    )

    # --------------------------------------------------

    print_separator(
        "STEP 2 - Execute"
    )

    result = executor.execute(
        plan,
        {
            "question": "Top selling products",
        },
    )

    print(result)

    assert (
        "steps"
        in result
    )

    assert (
        "context"
        in result
    )

    assert (
        len(
            result["steps"]
        )
        == 3
    )

    assert (
        result["steps"][0]
        == "retrieve"
    )

    assert (
        result["steps"][1]
        == "analytics"
    )

    assert (
        result["steps"][2]
        == "response"
    )

    assert (
        result["context"]["question"]
        == "Top selling products"
    )

    # --------------------------------------------------

    print_separator(
        "STEP 3 - Chart Plan"
    )

    plan = planner.build_plan(
        "Monthly sales chart"
    )

    print(
        plan.model_dump()
    )

    result = executor.execute(
        plan,
        {
            "question": "Monthly sales chart",
        },
    )

    print(result)

    assert (
        len(
            result["steps"]
        )
        == 4
    )

    assert (
        result["steps"][2]
        == "chart"
    )

    # --------------------------------------------------

    print()

    print("=" * 60)

    print("SUCCESS")

    print("=" * 60)

    print(
        "Execution Engine passed all manual tests."
    )


if __name__ == "__main__":

    main()