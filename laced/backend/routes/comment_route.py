from fastapi import APIRouter, Depends, HTTPException
from typing import List
from backend.controllers.comment_controller import CommentController
from backend.schemas.comment_schema import CommentSchema
from backend.utils.dependencies import get_current_user

router = APIRouter()
comment_ctrl = CommentController()

@router.get("/", response_model=List[CommentSchema])
async def list_comments():
    return await comment_ctrl.list_comments()

@router.post("/", response_model=CommentSchema)
async def add_comment(payload: CommentSchema, current_user=Depends(get_current_user)):
    try:
        return await comment_ctrl.add_comment(payload, current_user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{comment_id}", status_code=204)
async def delete_comment(comment_id: str, current_user=Depends(get_current_user)):
    await comment_ctrl.delete_comment(comment_id, current_user)
    return {"detail": "Deleted"}
