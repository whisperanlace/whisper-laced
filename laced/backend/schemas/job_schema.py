# schemas/job_schema.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class JobCreate(BaseModel):
    task_name: str
    parameters: Optional[dict] = None


class JobOut(BaseModel):
    id: int
    task_name: str
    status: str
    parameters: Optional[dict] = None
    created_at: datetime
    completed_at: Optional[datetime] = None

    class Config:
        orm_mode = True
