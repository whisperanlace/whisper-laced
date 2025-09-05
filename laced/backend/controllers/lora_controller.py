from fastapi import APIRouter, Depends, UploadFile, HTTPException
from backend.services import LoraService
from backend.utils.dependencies import get_current_user

router = APIRouter(prefix="/loras", tags=["LoRAs"])
lora_service = LoraService()

@router.get("/")
async def get_loras(user=Depends(get_current_user)):
    return await lora_service.get_loras(user)

@router.post("/upload")
async def upload_lora(file: UploadFile, user=Depends(get_current_user)):
    return await lora_service.upload_lora(file, user)

@router.delete("/{lora_id}")
async def delete_lora(lora_id: str, user=Depends(get_current_user)):
    success = await lora_service.delete_lora(lora_id, user)
    if not success:
        raise HTTPException(status_code=404, detail="LoRA not found")
    return {"detail": "LoRA deleted"}
