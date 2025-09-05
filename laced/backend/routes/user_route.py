from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from backend.schemas.user_schema import UserSchema, UserUpdateSchema
from backend.controllers.user_controller import UserController
from backend.utils.dependencies import get_current_user

router = APIRouter()
user_ctrl = UserController()

@router.get("/", response_model=List[UserSchema])
async def list_users():
    return await user_ctrl.list_users()

@router.get("/{user_id}", response_model=UserSchema)
async def get_user(user_id: str):
    return await user_ctrl.get_user(user_id)

@router.put("/{user_id}", response_model=UserSchema)
async def update_user(user_id: str, payload: UserUpdateSchema, current_user=Depends(get_current_user)):
    return await user_ctrl.update_user(user_id, payload, current_user)

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: str, current_user=Depends(get_current_user)):
    await user_ctrl.delete_user(user_id, current_user)
    return {"detail": "User deleted"}
