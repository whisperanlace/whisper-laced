from pydantic import BaseModel
from typing import Optional

class PremiumModelBase(BaseModel):
    name: str
    description: Optional[str] = None

class PremiumModelCreate(PremiumModelBase):
    tier_id: int

class PremiumModelResponse(PremiumModelBase):
    id: int
    tier_id: int
    is_active: bool

    class Config:
        from_attributes = True
