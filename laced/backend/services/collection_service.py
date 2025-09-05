# services/Collection_service.py
from sqlalchemy.orm import Session
from app.models.Collection import Collection
from fastapi import HTTPException, status

class CollectionService:
    async def create_collection(self, db: Session, user_id: int, name: str):
        collection = Collection(user_id=user_id, name=name)
        db.add(collection)
        db.commit()
        db.refresh(collection)
        return collection

    async def list_collections(self, db: Session, user_id: int):
        return db.query(Collection).filter(Collection.user_id == user_id).all()
