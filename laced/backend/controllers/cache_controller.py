# controllers/cache_controller.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.cache_service import CacheService
from utils.dependencies import get_db, get_current_user

router = APIRouter(prefix="/cache", tags=["Cache"])


@router.post("/clear")
def clear_cache(db: Session = Depends(get_db), user=Depends(get_current_user)):
    if not user.is_admin:
        return {"detail": "Unauthorized"}
    CacheService.clear_cache()
    return {"detail": "Cache cleared"}
