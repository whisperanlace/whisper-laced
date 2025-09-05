from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from typing import List
from backend.schemas.video_schema import VideoSchema
from backend.controllers.video_controller import VideoController
from backend.utils.dependencies import get_current_user

router = APIRouter()
video_ctrl = VideoController()

@router.get("/", response_model=List[VideoSchema])
async def list_videos(current_user=Depends(get_current_user)):
    return await video_ctrl.list_videos(current_user)

@router.post("/upload", response_model=VideoSchema)
async def upload_video(file: UploadFile = File(...), current_user=Depends(get_current_user)):
    try:
        return await video_ctrl.upload(file, current_user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{video_id}", status_code=204)
async def delete_video(video_id: str, current_user=Depends(get_current_user)):
    await video_ctrl.delete_video(video_id, current_user)
    return {"detail": "Deleted"}
