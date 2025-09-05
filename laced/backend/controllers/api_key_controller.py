# controllers/api_key_controller.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.api_key_schema import ApiKeyOut
from services.api_key_service import ApiKeyService
from utils.dependencies import get_db, get_current_user

router = APIRouter(prefix="/api-keys", tags=["API Keys"])


@router.post("/", response_model=ApiKeyOut)
def create_api_key(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return ApiKeyService.create_key(db, user.id)


@router.get("/", response_model=list[ApiKeyOut])
def list_api_keys(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return ApiKeyService.list_keys(db, user.id)


@router.delete("/{key_id}")
def revoke_api_key(key_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    success = ApiKeyService.revoke_key(db, user.id, key_id)
    if not success:
        raise HTTPException(status_code=404, detail="API key not found")
    return {"detail": "API key revoked"}
