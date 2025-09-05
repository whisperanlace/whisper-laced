from fastapi import APIRouter, Depends, HTTPException
from backend.schemas.prompt_schema import PromptSchema
from backend.services import PromptService
from backend.utils.dependencies import get_current_user

router = APIRouter(prefix="/prompts", tags=["Prompts"])
prompt_service = PromptService()

@router.post("/")
async def create_prompt(payload: PromptSchema, user=Depends(get_current_user)):
    return await prompt_service.create_prompt(payload, user)

@router.get("/")
async def get_prompts(user=Depends(get_current_user)):
    return await prompt_service.get_prompts(user)
