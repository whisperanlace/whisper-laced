from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from backend.db import get_db
from backend.schemas.tier_schema import TierCreate, TierUpdate, TierResponse
from backend.schemas.user_schema import UserResponse
from backend.services import premium_service
from backend.dependencies.roles import require_role

def create_tier(tier: TierCreate, db: Session = Depends(get_db)) -> TierResponse:
    return premium_service.create_tier(db, tier)

def list_tiers(db: Session = Depends(get_db)) -> List[TierResponse]:
    return premium_service.list_tiers(db)

def update_tier(tier_id: int, tier: TierUpdate, db: Session = Depends(get_db)) -> TierResponse:
    db_tier = premium_service.update_tier(db, tier_id, tier)
    if not db_tier:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tier not found")
    return db_tier

def delete_tier(tier_id: int, db: Session = Depends(get_db)) -> dict:
    success = premium_service.delete_tier(db, tier_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tier not found")
    return {"detail": "Tier deleted"}

def assign_user(user_id: int, tier_id: int, db: Session = Depends(get_db)) -> UserResponse:
    user = premium_service.assign_user_to_tier(db, user_id, tier_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User or Tier not found")
    return user
