from fastapi import APIRouter, Depends, HTTPException
from typing import List
from backend.controllers.image_controller import ImageController
from backend.schemas.image_schema import ImageSchema
from backend.utils.dependencies import get_current_user

router = APIRouter()
image_ctrl = ImageController()

@router.get("/", response_model=List[ImageSchema])
async def list_images(current_user=Depends(get_current_user)):
    return await image_ctrl.list_images(current_user)

@router.get("/{image_id}", response_model=ImageSchema)
async def get_image(image_id: str, current_user=Depends(get_current_user)):
    return await image_ctrl.get_image(image_id)

@router.delete("/{image_id}", status_code=204)
async def delete_image(image_id: str, current_user=Depends(get_current_user)):
    await image_ctrl.delete_image(image_id, current_user)
    return {"detail": "Deleted"}
