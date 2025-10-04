from sqlalchemy.orm import Session
from typing import List
from backend.models import Lounge, lounge_members

def create_lounge(db: Session, community_id: int, name: str, description: str | None) -> Lounge:
    l = Lounge(community_id=community_id, name=name, description=description)
    db.add(l)
    db.commit()
    db.refresh(l)
    return l

def add_member(db: Session, lounge_id: int, user_id: int) -> None:
    db.execute(lounge_members.insert().values(lounge_id=lounge_id, user_id=user_id))
    db.commit()

def list_lounges(db: Session, community_id: int | None = None) -> List[Lounge]:
    q = db.query(Lounge)
    if community_id:
        q = q.filter(Lounge.community_id == community_id)
    return q.all()

