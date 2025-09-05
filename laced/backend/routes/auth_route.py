from fastapi import APIRouter, Depends, HTTPException, status
from backend.schemas.auth_schema import LoginSchema, RegisterSchema, TokenSchema
from backend.controllers.auth_controller import AuthController
from backend.utils.dependencies import get_current_user

router = APIRouter()
auth_ctrl = AuthController()

@router.post("/register", response_model=TokenSchema, status_code=status.HTTP_201_CREATED)
async def register_user(payload: RegisterSchema):
    try:
        return await auth_ctrl.register(payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login", response_model=TokenSchema)
async def login_user(payload: LoginSchema):
    try:
        return await auth_ctrl.login(payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/me", response_model=TokenSchema)
async def get_me(current_user=Depends(get_current_user)):
    return current_user
