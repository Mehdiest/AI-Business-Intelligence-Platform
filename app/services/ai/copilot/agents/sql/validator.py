"""
Enterprise SQL Validator.
"""

from __future__ import annotations


class SQLValidator:
    """
    Prevent unsafe SQL execution.
    """

    BLOCKED = (

        "drop",

        "delete",

        "truncate",

        "update",

        "insert",

        "alter",

        "create",

        "attach",

        "detach",

    )

    def validate(
        self,
        sql: str,
    ) -> None:

        query = sql.lower()

        for keyword in self.BLOCKED:

            if keyword in query:

                raise ValueError(

                    f"Unsafe SQL detected: {keyword}"

                )