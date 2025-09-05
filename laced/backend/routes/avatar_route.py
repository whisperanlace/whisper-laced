# routes/Avatars_route.py
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.Avatar_schemas import AvatarSchema
from app.services.Avatar_service import AvatarService

router = APIRouter()
service = AvatarService()

@router.get("/", response_model=list[AvatarSchema])
async def list_avatars(db: Session = Depends(get_db)):
    return await service.list_avatars(db)

@router.post("/upload", response_model=AvatarSchema, status_code=status.HTTP_201_CREATED)
async def upload_avatar(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if file.content_type not in ["image/png", "image/jpeg"]:
        raise HTTPException(status_code=400, detail="Invalid file type")
    avatar = await service.upload_avatar(db, file)
    return avatar
