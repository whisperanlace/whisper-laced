from __future__ import annotations
from pydantic import BaseModel, Field
from typing import Optional, List

class EnhancementRequestCreate(BaseModel):
    prompt: str = Field(..., min_length=1)

class EnhancementRequestOut(BaseModel):
    id: int
    document_id: int
    requested_by: int
    prompt: str
    status: str

    class Config:
        from_attributes = True

class EnhancementVersionOut(BaseModel):
    id: int
    document_id: int
    parent_request_id: Optional[int] = None
    version_index: int
    url: Optional[str] = None
    notes: Optional[str] = None

    class Config:
        from_attributes = True
