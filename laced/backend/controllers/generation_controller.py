from fastapi import APIRouter, Depends, HTTPException
from backend.services import GenerationService
from backend.schemas.generation_schema import GenerationCreateSchema
from backend.utils.dependencies import get_current_user

router = APIRouter(prefix="/generations", tags=["Generations"])
generation_service = GenerationService()

@router.post("/")
async def create_generation(payload: GenerationCreateSchema, user=Depends(get_current_user)):
    return await generation_service.create_generation(payload, user)

@router.get("/")
async def list_generations(user=Depends(get_current_user)):
    return await generation_service.get_generations(user)

@router.delete("/{generation_id}")
async def delete_generation(generation_id: str, user=Depends(get_current_user)):
    ok = await generation_service.delete_generation(generation_id, user)
    if not ok:
        raise HTTPException(status_code=404, detail="Generation not found")
    return {"detail": "Generation deleted"}
