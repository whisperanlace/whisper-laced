from fastapi import APIRouter
# comment.py
router = APIRouter()
@router.post("/comments")
def post_comment(): pass
