from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from backend.controllers.editor_controller import EditorController
from backend.schemas.editor_schema import EditorSchema
from backend.utils.dependencies import get_current_user

router = APIRouter()
editor_ctrl = EditorController()

@router.post("/edit", response_model=EditorSchema)
async def edit_image(file: UploadFile = File(...), instructions: str = "", current_user=Depends(get_current_user)):
    try:
        return await editor_ctrl.edit(file, instructions, current_user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
