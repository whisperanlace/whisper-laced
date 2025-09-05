from fastapi import APIRouter, Depends, UploadFile, Form
from backend.services import EditorService
from backend.utils.dependencies import get_current_user

router = APIRouter(prefix="/editor", tags=["Editor"])
editor_service = EditorService()

@router.post("/edit")
async def edit_image(file: UploadFile, instructions: str = Form(...), user=Depends(get_current_user)):
    return await editor_service.edit_image(file, instructions, user)
