# services/System_flag_service.py
from sqlalchemy.orm import Session
from app.models.System_flag import SystemFlag

class SystemFlagService:
    async def create_flag(self, db: Session, name: str, value: bool):
        flag = SystemFlag(name=name, value=value)
        db.add(flag)
        db.commit()
        db.refresh(flag)
        return flag
