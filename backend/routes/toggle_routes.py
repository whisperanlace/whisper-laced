from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.models import Toggle
from backend.schemas.toggle_schema import ToggleCreate, ToggleResponse
from backend.services import toggle_service

router = APIRouter()

@router.post("/", response_model=ToggleResponse, summary="Create toggle")
def create_toggle(toggle: ToggleCreate, db: Session = Depends(get_db)):
    db_toggle = toggle_service.create_toggle(db, toggle)
    return db_toggle

@router.get("/", response_model=list[ToggleResponse], summary="List toggles")
def list_toggles(db: Session = Depends(get_db)):
    return toggle_service.get_toggles(db)

