from fastapi import APIRouter, Depends
from typing import List
from backend.controllers.search_controller import SearchController
from backend.schemas.search_schema import SearchResultSchema
from backend.utils.dependencies import get_current_user

router = APIRouter()
search_ctrl = SearchController()

@router.get("/", response_model=List[SearchResultSchema])
async def search(query: str, current_user=Depends(get_current_user)):
    return await search_ctrl.search(query, current_user)
