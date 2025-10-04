from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from backend.db import get_db
from backend.schemas.avatar_schema import AvatarCreate, AvatarResponse
from backend.services import avatar_service
from backend.dependencies.auth import get_current_user

router = APIRouter()

@router.post("/", response_model=AvatarResponse)
def create_avatar(avatar: AvatarCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return avatar_service.create_avatar(db, avatar, current_user.id)

@router.get("/", response_model=List[AvatarResponse])
def list_avatars(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return avatar_service.list_avatars(db)
