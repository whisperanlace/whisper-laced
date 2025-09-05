from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class WhisperPrompt(BaseModel):
    prompt_text: str
    metadata: Optional[dict] = {}

class WhisperSessionCreate(BaseModel):
    user_id: int
    session_name: str
    prompts: List[WhisperPrompt] = []

class WhisperSessionResponse(BaseModel):
    id: int
    user_id: int
    session_name: str
    prompts: List[WhisperPrompt]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
