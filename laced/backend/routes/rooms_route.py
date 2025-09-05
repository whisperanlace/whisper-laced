from fastapi import APIRouter, Depends, HTTPException
from typing import List
from backend.controllers.room_controller import RoomController
from backend.schemas.room_schema import RoomSchema
from backend.utils.dependencies import get_current_user

router = APIRouter()
room_ctrl = RoomController()

@router.get("/", response_model=List[RoomSchema])
async def list_rooms(current_user=Depends(get_current_user)):
    return await room_ctrl.list_rooms(current_user)

@router.post("/", response_model=RoomSchema)
async def create_room(payload: RoomSchema, current_user=Depends(get_current_user)):
    try:
        return await room_ctrl.create_room(payload, current_user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{room_id}", status_code=204)
async def delete_room(room_id: str, current_user=Depends(get_current_user)):
    await room_ctrl.delete_room(room_id, current_user)
    return {"detail": "Deleted"}
