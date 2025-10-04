from sqlalchemy.orm import Session
from typing import List
from backend.models import Community, community_members
from backend.models import User

def create_community(db: Session, owner_id: int, name: str, description: str | None) -> Community:
    c = Community(owner_id=owner_id, name=name, description=description)
    db.add(c)
    db.commit()
    db.refresh(c)
    # owner auto-joins
    db.execute(community_members.insert().values(community_id=c.id, user_id=owner_id))
    db.commit()
    return c

def add_member(db: Session, community_id: int, user_id: int) -> None:
    db.execute(community_members.insert().values(community_id=community_id, user_id=user_id))
    db.commit()

def list_communities(db: Session) -> List[Community]:
    return db.query(Community).all()

