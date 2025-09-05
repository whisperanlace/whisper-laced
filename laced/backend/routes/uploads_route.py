from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from typing import List
from backend.controllers.uploads_controller import UploadsController
from backend.schemas.upload_schema import UploadSchema
from backend.utils.dependencies import get_current_user

router = APIRouter()
uploads_ctrl = UploadsController()

@router.post("/file", response_model=UploadSchema)
async def upload_file(file: UploadFile = File(...), current_user=Depends(get_current_user)):
    try:
        return await uploads_ctrl.upload(file, current_user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[UploadSchema])
async def list_uploads(current_user=Depends(get_current_user)):
    return await uploads_ctrl.list_uploads(current_user)

@router.delete("/{upload_id}", status_code=204)
async def delete_upload(upload_id: str, current_user=Depends(get_current_user)):
    await uploads_ctrl.delete_upload(upload_id, current_user)
    return {"detail": "Deleted"}
