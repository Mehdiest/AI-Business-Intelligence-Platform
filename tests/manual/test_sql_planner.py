"""
Manual SQL planner test.
"""

from app.services.ai.copilot.agents.sql import (
    SQLPlanner,
)


def main():

    planner = SQLPlanner()

    plan = planner.build_plan(

        "Top selling product"

    )

    print()

    print(plan.model_dump())

    assert plan.requires_sql

    assert plan.target_table == "sales"

    assert plan.operation == "analytics"

    print()

    print("=" * 60)

    print("SUCCESS")

    print("=" * 60)

    print(

        "SQL Planner passed."

    )


if __name__ == "__main__":

    main()