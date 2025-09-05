from fastapi import APIRouter, Depends, HTTPException
from backend.schemas.user_schema import UserUpdateSchema
from backend.services import UserService
from backend.utils.dependencies import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])
user_service = UserService()

@router.get("/")
async def list_users():
    return await user_service.get_all_users()

@router.get("/{user_id}")
async def get_user(user_id: str):
    user = await user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}")
async def update_user(user_id: str, payload: UserUpdateSchema):
    user = await user_service.update_user(user_id, payload)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}")
async def delete_user(user_id: str):
    success = await user_service.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted"}
