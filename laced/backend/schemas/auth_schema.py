# schemas/auth_schema.py

from pydantic import BaseModel, EmailStr
from typing import Optional


class AuthLogin(BaseModel):
    email: EmailStr
    password: str


class AuthRegister(BaseModel):
    email: EmailStr
    password: str
    full_name: str
    username: Optional[str] = None


class AuthOut(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    username: Optional[str]

    class Config:
        orm_mode = True
