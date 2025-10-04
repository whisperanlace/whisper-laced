from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# --- Tier sub-schema ---
class TierOut(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float

    class Config:
        from_attributes = True

# --- User schemas ---
class UserBase(BaseModel):
    email: EmailStr
    username: str

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(UserBase):
    id: int
    role: str
    is_active: bool
    created_at: datetime
    tier: Optional[TierOut] = None   # 👈 this exposes the relationship

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class APIKeyResponse(BaseModel):
    api_key: str
    active: bool
