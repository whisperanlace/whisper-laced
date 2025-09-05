from fastapi import APIRouter, Depends, HTTPException
from typing import List
from backend.schemas.community_schema import CommunitySchema
from backend.controllers.community_controller import CommunityController
from backend.utils.dependencies import get_current_user

router = APIRouter()
community_ctrl = CommunityController()

@router.get("/", response_model=List[CommunitySchema])
async def list_communities():
    return await community_ctrl.list_communities()

@router.post("/", response_model=CommunitySchema)
async def create_community(payload: CommunitySchema, current_user=Depends(get_current_user)):
    try:
        return await community_ctrl.create_community(payload, current_user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{community_id}", status_code=204)
async def delete_community(community_id: str, current_user=Depends(get_current_user)):
    await community_ctrl.delete_community(community_id, current_user)
    return {"detail": "Deleted"}
