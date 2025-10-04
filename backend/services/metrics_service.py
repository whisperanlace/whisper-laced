from sqlalchemy.orm import Session
from backend.models import Metrics
from backend.schemas.metrics_schema import MetricsCreate

def create_metric(db: Session, data: MetricsCreate):
    metric = Metrics(**data.dict())
    db.add(metric)
    db.commit()
    db.refresh(metric)
    return metric

