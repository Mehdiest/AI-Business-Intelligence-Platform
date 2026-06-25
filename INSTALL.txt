
Replace:
app/models/warehouse.py
app/models/__init__.py

Then run:
alembic revision --autogenerate -m "initial star schema"
alembic upgrade head
