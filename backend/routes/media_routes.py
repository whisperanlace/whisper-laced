# backend/routes/media_routes.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from backend.db import get_db
from backend.models import Media
from backend.schemas.media_schema import MediaCreate, MediaResponse
from backend.dependencies.auth import get_current_user

router = APIRouter()

@router.post("/", response_model=MediaResponse, summary="Upload media")
def create_media(
    media_in: MediaCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    media = Media(**media_in.dict(), user_id=current_user.id)
    db.add(media)
    db.commit()
    db.refresh(media)
    return media

@router.get("/", response_model=List[MediaResponse], summary="List my media")
def list_media(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return db.query(Media).filter(Media.user_id == current_user.id).all()

@router.get("/{media_id}", response_model=MediaResponse, summary="Get media by ID")
def get_media(
    media_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    media = db.query(Media).filter(
        Media.id == media_id,
        Media.user_id == current_user.id
    ).first()
    if not media:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Media not found")
    return media

@router.delete("/{media_id}", summary="Delete media by ID")
def delete_media(
    media_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    media = db.query(Media).filter(
        Media.id == media_id,
        Media.user_id == current_user.id
    ).first()
    if not media:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Media not found")
    db.delete(media)
    db.commit()
    return {"detail": "Media deleted"}

