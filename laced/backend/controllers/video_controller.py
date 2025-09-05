from fastapi import APIRouter, Depends, UploadFile, HTTPException
from backend.services import VideoService
from backend.utils.dependencies import get_current_user

router = APIRouter(prefix="/videos", tags=["Videos"])
video_service = VideoService()

@router.get("/")
async def get_videos(user=Depends(get_current_user)):
    return await video_service.get_videos(user)

@router.post("/upload")
async def upload_video(file: UploadFile, user=Depends(get_current_user)):
    return await video_service.upload_video(file, user)

@router.delete("/{video_id}")
async def delete_video(video_id: str, user=Depends(get_current_user)):
    success = await video_service.delete_video(video_id, user)
    if not success:
        raise HTTPException(status_code=404, detail="Video not found")
    return {"detail": "Video deleted"}
