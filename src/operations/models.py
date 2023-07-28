from datetime import datetime

from sqlalchemy import (
    MetaData, Integer, String,
    TIMESTAMP, Table, Column
)

metadata = MetaData()

operation = Table(
    "operation",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("quantity", String),
    Column("figi", String),
    Column("instrument_type", String, nullable=False),
    Column("date", TIMESTAMP, default=datetime.utcnow),
    Column("type", String)
)
