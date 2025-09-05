# controllers/feature_controller.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.feature_schema import FeatureCreate, FeatureOut
from services.feature_service import FeatureService
from utils.dependencies import get_db, get_current_user

router = APIRouter(prefix="/features", tags=["Features"])


@router.post("/", response_model=FeatureOut)
def create_feature(
    feature: FeatureCreate, db: Session = Depends(get_db), user=Depends(get_current_user)
):
    if not user.is_admin:
        raise HTTPException(status_code=403, detail="Unauthorized")
    return FeatureService.create_feature(db, feature)


@router.get("/", response_model=list[FeatureOut])
def list_features(db: Session = Depends(get_db)):
    return FeatureService.list_features(db)
