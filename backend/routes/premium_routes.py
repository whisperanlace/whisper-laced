from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from backend.db import get_db
from backend.schemas.tier_schema import TierCreate, TierUpdate, TierResponse
from backend.schemas.user_schema import UserResponse
from backend.controllers import premium_controller
from backend.dependencies.roles import require_role
from pydantic import BaseModel

router = APIRouter()

class AssignRequest(BaseModel):
    user_id: int
    tier_id: int

@router.post("/tiers", response_model=TierResponse, summary="Create a tier")
def create_tier(tier: TierCreate, db: Session = Depends(get_db), current_user=Depends(require_role("admin"))):
    return premium_controller.create_tier(tier, db)

@router.get("/tiers", response_model=List[TierResponse], summary="List all tiers")
def list_tiers(db: Session = Depends(get_db)):
    return premium_controller.list_tiers(db)

@router.put("/tiers/{tier_id}", response_model=TierResponse, summary="Update a tier")
def update_tier(tier_id: int, tier: TierUpdate, db: Session = Depends(get_db), current_user=Depends(require_role("admin"))):
    return premium_controller.update_tier(tier_id, tier, db)

@router.delete("/tiers/{tier_id}", summary="Delete a tier")
def delete_tier(tier_id: int, db: Session = Depends(get_db), current_user=Depends(require_role("admin"))):
    return premium_controller.delete_tier(tier_id, db)

# NEW: assign user to tier
@router.post("/assign", response_model=UserResponse, summary="Assign user to a tier")
def assign_user(request: AssignRequest, db: Session = Depends(get_db), current_user=Depends(require_role("admin"))):
    return premium_controller.assign_user(request.user_id, request.tier_id, db)
