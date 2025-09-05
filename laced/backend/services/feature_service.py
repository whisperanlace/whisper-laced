# services/Feature_service.py
from sqlalchemy.orm import Session
from app.models.Feature import Feature

class FeatureService:
    async def create_feature(self, db: Session, name: str, enabled: bool):
        feature = Feature(name=name, enabled=enabled)
        db.add(feature)
        db.commit()
        db.refresh(feature)
        return feature
