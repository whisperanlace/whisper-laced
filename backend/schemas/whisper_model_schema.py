from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class WhisperPromptCreate(BaseModel):
    user_id: int
    prompt_text: str

class WhisperPromptResponse(BaseModel):
    id: int
    user_id: int
    prompt_text: str
    response_text: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True
