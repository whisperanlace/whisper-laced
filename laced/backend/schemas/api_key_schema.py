# schemas/api_key_schema.py

from pydantic import BaseModel
from datetime import datetime


class ApiKeyOut(BaseModel):
    id: int
    user_id: int
    key: str
    created_at: datetime
    revoked: bool

    class Config:
        orm_mode = True
