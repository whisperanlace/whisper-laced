# controllers/export_controller.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.export_service import ExportService
from utils.dependencies import get_db, get_current_user

router = APIRouter(prefix="/export", tags=["Export"])


@router.get("/images")
def export_images(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return ExportService.export_images(db, user.id)


@router.get("/collections")
def export_collections(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return ExportService.export_collections(db, user.id)
