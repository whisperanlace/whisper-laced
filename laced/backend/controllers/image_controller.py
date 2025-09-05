from fastapi import APIRouter, Depends, UploadFile, HTTPException
from backend.services import ImageService
from backend.utils.dependencies import get_current_user

router = APIRouter(prefix="/images", tags=["Images"])
image_service = ImageService()

@router.get("/")
async def list_images(user=Depends(get_current_user)):
    return await image_service.get_user_images(user)

@router.get("/{image_id}")
async def get_image(image_id: str, user=Depends(get_current_user)):
    image = await image_service.get_image_by_id(image_id, user)
    if not image:
        raise HTTPException(status_code=404, detail="Image not found")
    return image

@router.delete("/{image_id}")
async def delete_image(image_id: str, user=Depends(get_current_user)):
    success = await image_service.delete_image(image_id, user)
    if not success:
        raise HTTPException(status_code=404, detail="Image not found")
    return {"detail": "Image deleted"}
