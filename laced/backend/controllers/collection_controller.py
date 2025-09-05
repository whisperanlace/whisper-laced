from fastapi import APIRouter, Depends, HTTPException
from backend.services import CollectionService
from backend.schemas.collection_schema import CollectionSchema
from backend.utils.dependencies import get_current_user

router = APIRouter(prefix="/collections", tags=["Collections"])
collection_service = CollectionService()

@router.get("/")
async def list_collections(user=Depends(get_current_user)):
    return await collection_service.get_collections(user)

@router.post("/")
async def create_collection(payload: CollectionSchema, user=Depends(get_current_user)):
    return await collection_service.create_collection(payload, user)

@router.delete("/{collection_id}")
async def delete_collection(collection_id: str, user=Depends(get_current_user)):
    ok = await collection_service.delete_collection(collection_id, user)
    if not ok:
        raise HTTPException(status_code=404, detail="Collection not found")
    return {"detail": "Collection deleted"}
