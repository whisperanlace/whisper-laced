from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.models import User
from backend.db import get_db
from backend.dependencies.auth import get_current_user
from backend.schemas.user_schema import UserResponse

router = APIRouter()

@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user

