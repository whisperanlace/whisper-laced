from fastapi import APIRouter, Depends, HTTPException
from backend.services import CommunityService
from backend.schemas.community_schema import CommunitySchema
from backend.utils.dependencies import get_current_user

router = APIRouter(prefix="/communities", tags=["Community"])
community_service = CommunityService()

@router.get("/")
async def list_communities():
    return await community_service.get_all_communities()

@router.post("/")
async def create_community(payload: CommunitySchema, user=Depends(get_current_user)):
    return await community_service.create_community(payload, user)

@router.delete("/{community_id}")
async def delete_community(community_id: str, user=Depends(get_current_user)):
    success = await community_service.delete_community(community_id, user)
    if not success:
        raise HTTPException(status_code=403, detail="Not authorized or community not found")
    return {"detail": "Community deleted"}
