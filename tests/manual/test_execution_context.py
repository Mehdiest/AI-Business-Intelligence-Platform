"""
Manual test for Execution Context.
"""

from __future__ import annotations

from app.services.ai.copilot.context_runtime import (
    ExecutionContextFactory,
)


def print_separator(
    title: str,
) -> None:

    print()

    print("=" * 60)

    print(title)

    print("=" * 60)


def main() -> None:

    print_separator(
        "STEP 1 - Create Context"
    )

    context = (
        ExecutionContextFactory.create(
            "Top selling product"
        )
    )

    print(
        context.model_dump()
    )

    assert (
        context.question
        == "Top selling product"
    )

    assert (
        context.intent
        is None
    )

    assert (
        context.plan
        is None
    )

    assert (
        context.retrieved_context
        is None
    )

    print_separator(
        "STEP 2 - Update Runtime"
    )

    context.response = (
        "Laptop is the best-selling product."
    )

    context.metadata[
        "version"
    ] = "1.0"

    print(
        context.model_dump()
    )

    assert (
        context.response
        == "Laptop is the best-selling product."
    )

    assert (
        context.metadata[
            "version"
        ]
        == "1.0"
    )

    print()

    print("=" * 60)

    print("SUCCESS")

    print("=" * 60)

    print(
        "Execution Context passed all manual tests."
    )


if __name__ == "__main__":

    main()