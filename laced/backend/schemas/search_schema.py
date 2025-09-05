# schemas/search_schema.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SearchSchema(BaseModel):
    id: int
    user_id: int
    query: str
    created_at: datetime

    class Config:
        orm_mode = True

class SearchCreateSchema(BaseModel):
    user_id: int
    query: str
