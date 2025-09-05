# schemas/subscription_schema.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class SubscriptionCreate(BaseModel):
    plan_id: int
    start_date: Optional[datetime] = None


class SubscriptionOut(BaseModel):
    id: int
    user_id: int
    plan_id: int
    start_date: datetime
    end_date: Optional[datetime]
    active: bool

    class Config:
        orm_mode = True
