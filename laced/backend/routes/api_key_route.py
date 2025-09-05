from fastapi import APIRouter, Depends, HTTPException
from typing import List
from backend.controllers.api_key_controller import ApiKeyController
from backend.schemas.api_key_schema import ApiKeySchema
from backend.utils.dependencies import get_current_user

router = APIRouter()
api_ctrl = ApiKeyController()

@router.get("/", response_model=List[ApiKeySchema])
async def list_keys(current_user=Depends(get_current_user)):
    return await api_ctrl.list_keys(current_user)

@router.post("/", response_model=ApiKeySchema)
async def create_key(current_user=Depends(get_current_user)):
    try:
        return await api_ctrl.create_key(current_user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{key_id}", status_code=204)
async def delete_key(key_id: str, current_user=Depends(get_current_user)):
    await api_ctrl.delete_key(key_id, current_user)
    return {"detail": "Deleted"}
