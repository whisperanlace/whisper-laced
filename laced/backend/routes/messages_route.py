from fastapi import APIRouter, Depends, HTTPException
from typing import List
from backend.controllers.message_controller import MessageController
from backend.schemas.message_schema import MessageSchema
from backend.utils.dependencies import get_current_user

router = APIRouter()
msg_ctrl = MessageController()

@router.get("/", response_model=List[MessageSchema])
async def list_messages(current_user=Depends(get_current_user)):
    return await msg_ctrl.list_messages(current_user)

@router.post("/", response_model=MessageSchema)
async def send_message(payload: MessageSchema, current_user=Depends(get_current_user)):
    try:
        return await msg_ctrl.send_message(payload, current_user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{message_id}", status_code=204)
async def delete_message(message_id: str, current_user=Depends(get_current_user)):
    await msg_ctrl.delete_message(message_id, current_user)
    return {"detail": "Deleted"}
