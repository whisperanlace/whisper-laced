# schemas/billing_schema.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class BillingOut(BaseModel):
    id: int
    user_id: int
    amount: float
    currency: str
    status: str
    created_at: datetime
    paid_at: Optional[datetime]
