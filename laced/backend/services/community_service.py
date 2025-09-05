# services/Community_service.py
from sqlalchemy.orm import Session
from app.models.Community import Community
from fastapi import HTTPException, status

class CommunityService:
    async def create_community(self, db: Session, name: str, description: str):
        existing = db.query(Community).filter(Community.name == name).first()
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Community name already exists")
        community = Community(name=name, description=description)
        db.add(community)
        db.commit()
        db.refresh(community)
        return community

    async def list_communities(self, db: Session):
        return db.query(Community).all()

    async def get_community(self, db: Session, community_id: int):
        community = db.query(Community).filter(Community.id == community_id).first()
        if not community:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return community
