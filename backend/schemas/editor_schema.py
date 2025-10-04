from __future__ import annotations
from pydantic import BaseModel, Field
from typing import Optional, List

class EditorDocumentCreate(BaseModel):
    title: str = Field(..., max_length=255)
    media_id: Optional[int] = None

class EditorDocumentOut(BaseModel):
    id: int
    owner_id: int
    title: str
    media_id: Optional[int] = None

    class Config:
        from_attributes = True
