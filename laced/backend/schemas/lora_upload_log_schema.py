# schemas/lora_upload_log_schema.py

from pydantic import BaseModel
from datetime import datetime


class LoraUploadLogOut(BaseModel):
    id: int
    user_id: int
    lora_id: int
    status: str
    created_at: datetime

    class Config:
        orm_mode = True
