"""
Manual test for the Planner Agent.
"""

from __future__ import annotations

from app.services.ai.copilot.agents.planner import (
    PlannerAgent,
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

    # --------------------------------------------------

    print_separator(
        "TEST 1 - Product Question"
    )

    plan = planner.build_plan(
        "Top selling products"
    )

    print(
        plan.model_dump()
    )

    assert (
        len(plan.steps) == 3
    )

    assert (
        plan.steps[0].value
        == "retrieve"
    )

    assert (
        plan.steps[1].value
        == "analytics"
    )

    assert (
        plan.steps[2].value
        == "response"
    )

    # --------------------------------------------------

    print_separator(
        "TEST 2 - Chart Question"
    )

    plan = planner.build_plan(
        "Show monthly sales chart"
    )

    print(
        plan.model_dump()
    )

    assert (
        len(plan.steps) == 4
    )

    assert (
        plan.steps[0].value
        == "retrieve"
    )

    assert (
        plan.steps[1].value
        == "analytics"
    )

    assert (
        plan.steps[2].value
        == "chart"
    )

    assert (
        plan.steps[3].value
        == "response"
    )

    # --------------------------------------------------

    print_separator(
        "TEST 3 - Generic Question"
    )

    plan = planner.build_plan(
        "Hello"
    )

    print(
        plan.model_dump()
    )

    assert (
        len(plan.steps) == 2
    )

    assert (
        plan.steps[0].value
        == "retrieve"
    )

    assert (
        plan.steps[1].value
        == "response"
    )

    # --------------------------------------------------

    print()

    print("=" * 60)

    print("SUCCESS")

    print("=" * 60)

    print(
        "Planner Agent passed all manual tests."
    )


if __name__ == "__main__":

    main()