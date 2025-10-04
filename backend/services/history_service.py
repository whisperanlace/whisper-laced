from sqlalchemy.orm import Session
from backend.models import History
from backend.schemas.history_schema import HistoryCreate

def create_history(db: Session, data: HistoryCreate):
    history = History(**data.dict())
    db.add(history)
    db.commit()
    db.refresh(history)
    return history

def get_user_history(db: Session, user_id: int):
    return db.query(History).filter(History.user_id == user_id).all()

