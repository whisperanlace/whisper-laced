from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from typing import List
from backend.schemas.lora_schema import LoraSchema
from backend.controllers.lora_controller import LoraController
from backend.utils.dependencies import get_current_user

router = APIRouter()
lora_ctrl = LoraController()

@router.get("/", response_model=List[LoraSchema])
async def list_loras(current_user=Depends(get_current_user)):
    return await lora_ctrl.list_loras(current_user)

@router.post("/upload", response_model=LoraSchema)
async def upload_lora(file: UploadFile = File(...), current_user=Depends(get_current_user)):
    try:
        return await lora_ctrl.upload(file, current_user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{lora_id}", status_code=204)
async def delete_lora(lora_id: str, current_user=Depends(get_current_user)):
    await lora_ctrl.delete_lora(lora_id, current_user)
    return {"detail": "Deleted"}
