from fastapi import APIRouter, Depends, UploadFile, HTTPException
from backend.services import UploadService
from backend.utils.dependencies import get_current_user

router = APIRouter(prefix="/uploads", tags=["Uploads"])
upload_service = UploadService()

@router.post("/")
async def upload_file(file: UploadFile, user=Depends(get_current_user)):
    return await upload_service.upload_file(file, user)

@router.get("/")
async def list_uploads(user=Depends(get_current_user)):
    return await upload_service.get_uploads(user)

@router.delete("/{upload_id}")
async def delete_upload(upload_id: str, user=Depends(get_current_user)):
    ok = await upload_service.delete_upload(upload_id, user)
    if not ok:
        raise HTTPException(status_code=404, detail="Upload not found")
    return {"detail": "Upload deleted"}
