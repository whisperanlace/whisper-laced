# controllers/tier_controller.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.tier_schema import TierCreate, TierOut
from services.tier_service import TierService
from utils.dependencies import get_db, get_current_user

router = APIRouter(prefix="/tiers", tags=["Tiers"])


@router.post("/", response_model=TierOut)
def create_tier(
    tier: TierCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    if not user.is_admin:
        raise HTTPException(status_code=403, detail="Unauthorized")
    return TierService.create_tier(db, tier)


@router.get("/", response_model=list[TierOut])
def list_tiers(db: Session = Depends(get_db)):
    return TierService.list_tiers(db)


@router.delete("/{tier_id}")
def delete_tier(
    tier_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    if not user.is_admin:
        raise HTTPException(status_code=403, detail="Unauthorized")
    success = TierService.delete_tier(db, tier_id)
    if not success:
        raise HTTPException(status_code=404, detail="Tier not found")
    return {"detail": "Tier deleted"}
