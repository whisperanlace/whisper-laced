from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.schemas.history_schema import HistoryCreate, HistoryResponse
from backend.services.history_service import create_history, get_user_history

router = APIRouter()

@router.post("/", response_model=HistoryResponse)
def add_history(data: HistoryCreate, db: Session = Depends(get_db)):
    return create_history(db, data)

@router.get("/user/{user_id}", response_model=list[HistoryResponse])
def list_user_history(user_id: int, db: Session = Depends(get_db)):
    return get_user_history(db, user_id)
@router.get("/")
def get_history_root():
    return {"message": "History endpoint reached"}
