"""
CSV ingestion service.

Responsibilities:
- Validate uploaded CSV files
- Load data into pandas DataFrame
- Standardize column names
- Handle malformed files safely
- Return clean DataFrames for downstream ETL stages
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


class CSVLoaderError(Exception):
    """Raised when CSV ingestion fails."""


class CSVLoader:
    """
    Production-oriented CSV loader.

    Example:
        loader = CSVLoader()
        df = loader.load("data/sales.csv")
    """

    REQUIRED_COLUMNS = {
        "customer_code",
        "customer_name",
        "product_code",
        "product_name",
        "region",
        "channel",
        "sale_date",
        "quantity",
        "amount",
    }

    def load(self, file_path: str | Path) -> pd.DataFrame:
        """
        Load CSV file into DataFrame.

        Args:
            file_path: Path to CSV file

        Returns:
            Clean pandas DataFrame

        Raises:
            CSVLoaderError
        """

        file_path = Path(file_path)

        if not file_path.exists():
            raise CSVLoaderError(
                f"CSV file not found: {file_path}"
            )

        if file_path.suffix.lower() != ".csv":
            raise CSVLoaderError(
                "Only CSV files are supported."
            )

        try:
            df = pd.read_csv(file_path)
        except Exception as exc:
            raise CSVLoaderError(
                f"Failed to read CSV file: {exc}"
            ) from exc

        if df.empty:
            raise CSVLoaderError(
                "CSV file contains no rows."
            )

        df.columns = [
            column.strip().lower()
            for column in df.columns
        ]

        self._validate_columns(df)

        return df

    def _validate_columns(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        """
        Validate required columns.
        """

        missing_columns = (
            self.REQUIRED_COLUMNS
            - set(dataframe.columns)
        )

        if missing_columns:
            raise CSVLoaderError(
                "Missing required columns: "
                + ", ".join(sorted(missing_columns))
            )