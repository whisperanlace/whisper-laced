from fastapi import APIRouter, Depends, HTTPException
from typing import List
from backend.controllers.post_controller import PostController
from backend.schemas.post_schema import PostSchema
from backend.utils.dependencies import get_current_user

router = APIRouter()
post_ctrl = PostController()

@router.get("/", response_model=List[PostSchema])
async def list_posts():
    return await post_ctrl.list_posts()

@router.post("/", response_model=PostSchema)
async def create_post(payload: PostSchema, current_user=Depends(get_current_user)):
    try:
        return await post_ctrl.create_post(payload, current_user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{post_id}", status_code=204)
async def delete_post(post_id: str, current_user=Depends(get_current_user)):
    await post_ctrl.delete_post(post_id, current_user)
    return {"detail": "Deleted"}
