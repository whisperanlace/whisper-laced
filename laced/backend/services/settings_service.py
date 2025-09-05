# services/Settings_service.py
from sqlalchemy.orm import Session
from app.models.Settings import Settings
from fastapi import HTTPException, status

class SettingsService:
    async def get_settings(self, db: Session):
        return db.query(Settings).first()

    async def update_settings(self, db: Session, updates: dict):
        settings = await self.get_settings(db)
        for key, value in updates.items():
            setattr(settings, key, value)
        db.commit()
        db.refresh(settings)
        return settings
