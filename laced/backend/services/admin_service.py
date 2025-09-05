# services/Admin_service.py
from sqlalchemy.orm import Session
from app.models.Admin import Admin
from fastapi import HTTPException, status

class AdminService:
    async def create_admin(self, db: Session, email: str):
        existing = db.query(Admin).filter(Admin.email == email).first()
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Admin exists")
        admin = Admin(email=email)
        db.add(admin)
        db.commit()
        db.refresh(admin)
        return admin

    async def list_admins(self, db: Session):
        return db.query(Admin).all()
