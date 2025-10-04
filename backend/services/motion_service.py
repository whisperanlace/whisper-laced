from sqlalchemy.orm import Session
from backend.models import Motion

def create_motion(db: Session, created_by: int, title: str, description: str | None, community_id: int | None, lounge_id: int | None) -> Motion:
    m = Motion(created_by=created_by, title=title, description=description, community_id=community_id, lounge_id=lounge_id)
    db.add(m)
    db.commit()
    db.refresh(m)
    return m

