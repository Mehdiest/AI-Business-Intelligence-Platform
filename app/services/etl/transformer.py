"""
Data transformation layer.

Responsibilities:
- Clean incoming records
- Standardize datatypes
- Handle missing values
- Apply business validation rules
- Prepare records for warehouse loading
"""

from __future__ import annotations

import pandas as pd


class TransformationError(Exception):
    """Raised when data transformation fails."""


class DataTransformer:
    """
    Production ETL transformation service.
    """

    REQUIRED_COLUMNS = [
        "customer_code",
        "customer_name",
        "product_code",
        "product_name",
        "region",
        "channel",
        "sale_date",
        "quantity",
        "amount",
    ]

    def transform(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Execute transformation pipeline.
        """

        dataframe = dataframe.copy()

        self._validate_required_columns(dataframe)

        dataframe = self._normalize_strings(dataframe)

        dataframe["sale_date"] = pd.to_datetime(
            dataframe["sale_date"],
            errors="coerce",
        )

        dataframe["quantity"] = pd.to_numeric(
            dataframe["quantity"],
            errors="coerce",
        )

        dataframe["amount"] = pd.to_numeric(
            dataframe["amount"],
            errors="coerce",
        )

        dataframe = dataframe.dropna(
            subset=[
                "sale_date",
                "quantity",
                "amount",
            ]
        )

        dataframe = dataframe[
            dataframe["quantity"] > 0
        ]

        dataframe = dataframe[
            dataframe["amount"] > 0
        ]

        dataframe = dataframe.drop_duplicates()

        dataframe.reset_index(
            drop=True,
            inplace=True,
        )

        return dataframe

    def _validate_required_columns(
        self,
        dataframe: pd.DataFrame,
    ) -> None:

        missing = (
            set(self.REQUIRED_COLUMNS)
            - set(dataframe.columns)
        )

        if missing:
            raise TransformationError(
                "Missing required columns: "
                + ", ".join(sorted(missing))
            )

    @staticmethod
    def _normalize_strings(
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:

        string_columns = [
            "customer_code",
            "customer_name",
            "product_code",
            "product_name",
            "region",
            "channel",
        ]

        for column in string_columns:
            dataframe[column] = (
                dataframe[column]
                .astype(str)
                .str.strip()
            )

        return dataframe