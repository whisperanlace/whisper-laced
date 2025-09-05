from fastapi import APIRouter, Depends, HTTPException
from backend.services import MessageService
from backend.schemas.message_schema import MessageSchema
from backend.utils.dependencies import get_current_user

router = APIRouter(prefix="/messages", tags=["Messages"])
message_service = MessageService()

@router.get("/")
async def get_messages(user=Depends(get_current_user)):
    return await message_service.get_messages(user)

@router.post("/")
async def send_message(payload: MessageSchema, user=Depends(get_current_user)):
    return await message_service.send_message(payload, user)

@router.delete("/{message_id}")
async def delete_message(message_id: str, user=Depends(get_current_user)):
    success = await message_service.delete_message(message_id, user)
    if not success:
        raise HTTPException(status_code=404, detail="Message not found")
    return {"detail": "Message deleted"}
