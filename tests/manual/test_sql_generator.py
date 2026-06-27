"""
Manual SQL Generator test.
"""

from app.services.ai.copilot.agents.sql.generator import (
    SQLGenerator,
)

from app.services.ai.copilot.agents.sql.models import (
    SQLPlan,
)

from app.services.ai.copilot.agents.sql.validator import (
    SQLValidator,
)


def main():

    plan = SQLPlan(

        requires_sql=True,

        target_table="sales",

        operation="analytics",

        explanation="demo",

    )

    generator = SQLGenerator()

    validator = SQLValidator()

    result = generator.generate(

        "Top selling product",

        plan,

    )

    print()

    print(result.model_dump())

    validator.validate(

        result.sql

    )

    assert (

        "SELECT"

        in result.sql.upper()

    )

    assert (

        "DROP"

        not in result.sql.upper()

    )

    print()

    print("=" * 60)

    print("SUCCESS")

    print("=" * 60)

    print(

        "SQL Generator passed."

    )


if __name__ == "__main__":

    main()