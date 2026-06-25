"""
Warehouse loading service.

Responsibilities:
- Load transformed data into warehouse dimensions
- Populate fact table
- Prevent duplicate dimensions
- Manage transactional inserts
"""

from __future__ import annotations

from sqlalchemy.orm import Session

from app.models.warehouse import (
    DimChannel,
    DimCustomer,
    DimDate,
    DimProduct,
    DimRegion,
    FactSales,
)


class WarehouseLoader:
    """
    Loads transformed data into the warehouse.
    """

    def __init__(self, db: Session):
        self.db = db

    def load_dataframe(self, dataframe):
        """
        Load transformed dataframe into warehouse.
        """

        loaded_rows = 0

        for _, row in dataframe.iterrows():

            customer = self._get_or_create_customer(
                row["customer_code"],
                row["customer_name"],
            )

            product = self._get_or_create_product(
                row["product_code"],
                row["product_name"],
            )

            region = self._get_or_create_region(
                row["region"]
            )

            channel = self._get_or_create_channel(
                row["channel"]
            )

            date_dimension = self._get_or_create_date(
                row["sale_date"]
            )

            fact_record = FactSales(
                customer_id=customer.id,
                product_id=product.id,
                region_id=region.id,
                channel_id=channel.id,
                date_id=date_dimension.id,
                quantity=int(row["quantity"]),
                amount=float(row["amount"]),
            )

            self.db.add(fact_record)

            loaded_rows += 1

        self.db.commit()

        return loaded_rows

    def _get_or_create_customer(
        self,
        customer_code: str,
        customer_name: str,
    ):

        customer = (
            self.db.query(DimCustomer)
            .filter(
                DimCustomer.customer_code
                == customer_code
            )
            .first()
        )

        if customer:
            return customer

        customer = DimCustomer(
            customer_code=customer_code,
            customer_name=customer_name,
        )

        self.db.add(customer)
        self.db.flush()

        return customer

    def _get_or_create_product(
        self,
        product_code: str,
        product_name: str,
    ):

        product = (
            self.db.query(DimProduct)
            .filter(
                DimProduct.product_code
                == product_code
            )
            .first()
        )

        if product:
            return product

        product = DimProduct(
            product_code=product_code,
            product_name=product_name,
        )

        self.db.add(product)
        self.db.flush()

        return product

    def _get_or_create_region(
        self,
        region_name: str,
    ):

        region = (
            self.db.query(DimRegion)
            .filter(
                DimRegion.region_name
                == region_name
            )
            .first()
        )

        if region:
            return region

        region = DimRegion(
            region_name=region_name
        )

        self.db.add(region)
        self.db.flush()

        return region

    def _get_or_create_channel(
        self,
        channel_name: str,
    ):

        channel = (
            self.db.query(DimChannel)
            .filter(
                DimChannel.channel_name
                == channel_name
            )
            .first()
        )

        if channel:
            return channel

        channel = DimChannel(
            channel_name=channel_name
        )

        self.db.add(channel)
        self.db.flush()

        return channel

    def _get_or_create_date(
        self,
        sale_date,
    ):

        existing = (
            self.db.query(DimDate)
            .filter(
                DimDate.full_date
                == sale_date.date()
            )
            .first()
        )

        if existing:
            return existing

        date_dimension = DimDate(
            full_date=sale_date.date()
        )

        self.db.add(date_dimension)
        self.db.flush()

        return date_dimension