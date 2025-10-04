from sqlalchemy.orm import Session
from backend.models import Tier
from backend.models import User
from backend.schemas.tier_schema import TierCreate, TierUpdate
from typing import List, Optional

def create_tier(db: Session, tier: TierCreate) -> Tier:
    db_tier = Tier(**tier.dict())
    db.add(db_tier)
    db.commit()
    db.refresh(db_tier)
    return db_tier

def list_tiers(db: Session) -> List[Tier]:
    return db.query(Tier).all()

def update_tier(db: Session, tier_id: int, tier: TierUpdate) -> Optional[Tier]:
    db_tier = db.query(Tier).filter(Tier.id == tier_id).first()
    if not db_tier:
        return None
    for key, value in tier.dict(exclude_unset=True).items():
        setattr(db_tier, key, value)
    db.commit()
    db.refresh(db_tier)
    return db_tier

def delete_tier(db: Session, tier_id: int) -> bool:
    db_tier = db.query(Tier).filter(Tier.id == tier_id).first()
    if not db_tier:
        return False
    db.delete(db_tier)
    db.commit()
    return True

# NEW: assign user to tier
def assign_user_to_tier(db: Session, user_id: int, tier_id: int) -> Optional[User]:
    user = db.query(User).filter(User.id == user_id).first()
    tier = db.query(Tier).filter(Tier.id == tier_id).first()
    if not user or not tier:
        return None
    user.tier_id = tier_id
    db.commit()
    db.refresh(user)
    return user

