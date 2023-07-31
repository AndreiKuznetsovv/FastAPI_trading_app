from datetime import datetime

from sqlalchemy import (
    Integer, String,
    TIMESTAMP, Table, Column
)

from src.database import metadata

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
