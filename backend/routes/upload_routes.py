from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from backend.db import get_db
from backend.schemas.upload_schema import UploadCreate, UploadResponse
from backend.services import upload_service
from backend.dependencies.auth import get_current_user

router = APIRouter()

@router.post("/", response_model=UploadResponse)
def upload_file(upload: UploadCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return upload_service.create_upload(db, upload, current_user.id)

@router.get("/", response_model=List[UploadResponse])
def list_uploads(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return upload_service.list_uploads(db)
