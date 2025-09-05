from fastapi import APIRouter, Depends, UploadFile, HTTPException
from backend.services import AvatarService
from backend.utils.dependencies import get_current_user

router = APIRouter(prefix="/avatars", tags=["Avatars"])
avatar_service = AvatarService()

@router.get("/")
async def get_avatars(user=Depends(get_current_user)):
    return await avatar_service.get_avatars(user)

@router.post("/upload")
async def upload_avatar(file: UploadFile, user=Depends(get_current_user)):
    return await avatar_service.upload_avatar(file, user)

@router.delete("/{avatar_id}")
async def delete_avatar(avatar_id: str, user=Depends(get_current_user)):
    success = await avatar_service.delete_avatar(avatar_id, user)
    if not success:
        raise HTTPException(status_code=404, detail="Avatar not found")
    return {"detail": "Avatar deleted"}
