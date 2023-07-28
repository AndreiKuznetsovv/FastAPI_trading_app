from pydantic import BaseModel
from datetime import datetime

class OperationCreate(BaseModel):
    quantity: str
    figi: str
    instrument_type: str
    date: datetime
    type: str
