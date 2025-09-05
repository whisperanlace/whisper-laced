# routes/Collections_route.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.Collection_schemas import CollectionSchema
from app.services.Collection_service import CollectionService

router = APIRouter()
service = CollectionService()

@router.get("/", response_model=list[CollectionSchema])
async def list_collections(db: Session = Depends(get_db)):
    return await service.list_collections(db)

@router.post("/", response_model=CollectionSchema)
async def create_collection(payload: CollectionSchema, db: Session = Depends(get_db)):
    return await service.create_collection(db, payload)
