# schemas/webhook_schema.py

from pydantic import BaseModel
from typing import Optional


class WebhookCreate(BaseModel):
    url: str
    event: str
    active: bool = True


class WebhookOut(BaseModel):
    id: int
    url: str
    event: str
    active: bool

    class Config:
        orm_mode = True
