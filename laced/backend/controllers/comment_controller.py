from fastapi import HTTPException
from typing import List
from backend.services.comment_service import CommentService
from backend.schemas.comment_schema import CommentSchema

comment_service = CommentService()

class CommentController:

    async def list_comments(self) -> List[CommentSchema]:
        return await comment_service.get_all_comments()

    async def add_comment(self, payload, current_user) -> CommentSchema:
        try:
            return await comment_service.add_comment(payload, current_user)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    async def delete_comment(self, comment_id: str, current_user):
        success = await comment_service.delete_comment(comment_id, current_user)
        if not success:
            raise HTTPException(status_code=400, detail="Could not delete comment")
