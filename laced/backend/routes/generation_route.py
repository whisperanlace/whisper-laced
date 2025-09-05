from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from typing import List
from backend.schemas.prompt_schema import PromptSchema
from backend.schemas.image_schema import ImageSchema
from backend.controllers.generation_controller import GenerationController
from backend.utils.dependencies import get_current_user

router = APIRouter()
gen_ctrl = GenerationController()

@router.post("/", response_model=ImageSchema)
async def generate_image(payload: PromptSchema, current_user=Depends(get_current_user)):
    try:
        return await gen_ctrl.generate(payload, current_user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/batch", response_model=List[ImageSchema])
async def generate_batch(prompts: List[PromptSchema], current_user=Depends(get_current_user)):
    return await gen_ctrl.generate_batch(prompts, current_user)
