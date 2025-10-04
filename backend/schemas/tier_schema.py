from pydantic import BaseModel
from typing import Optional


class TierBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float


class TierCreate(TierBase):
    pass


class TierUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None


class TierResponse(TierBase):
    id: int

    class Config:
        from_attributes = True
