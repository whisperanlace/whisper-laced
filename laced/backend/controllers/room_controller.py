from fastapi import APIRouter, Depends, HTTPException
from backend.services import RoomService
from backend.schemas.room_schema import RoomSchema
from backend.utils.dependencies import get_current_user

router = APIRouter(prefix="/rooms", tags=["Rooms"])
room_service = RoomService()

@router.get("/")
async def get_rooms(user=Depends(get_current_user)):
    return await room_service.get_rooms(user)

@router.post("/")
async def create_room(payload: RoomSchema, user=Depends(get_current_user)):
    return await room_service.create_room(payload, user)

@router.delete("/{room_id}")
async def delete_room(room_id: str, user=Depends(get_current_user)):
    success = await room_service.delete_room(room_id, user)
    if not success:
        raise HTTPException(status_code=404, detail="Room not found")
    return {"detail": "Room deleted"}
