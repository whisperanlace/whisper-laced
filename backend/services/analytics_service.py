from sqlalchemy.orm import Session
from backend.models import Analytics
from backend.schemas.analytics_schema import AnalyticsCreate

def create_analytics(db: Session, data: AnalyticsCreate):
    analytics = Analytics(**data.dict())
    db.add(analytics)
    db.commit()
    db.refresh(analytics)
    return analytics

