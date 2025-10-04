from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.schemas.analytics_schema import AnalyticsCreate, AnalyticsResponse
from backend.services.analytics_service import create_analytics

router = APIRouter()

@router.post("/", response_model=AnalyticsResponse)
def add_analytics(data: AnalyticsCreate, db: Session = Depends(get_db)):
    return create_analytics(db, data)
@router.get("/")
def get_analytics_root():
    return {"message": "Analytics endpoint reached"}
