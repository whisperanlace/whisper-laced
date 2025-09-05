from fastapi import APIRouter, Depends, HTTPException, status
from backend.schemas.auth_schema import LoginSchema, RegisterSchema
from backend.services import AuthService
from backend.utils.dependencies import get_current_user

router = APIRouter(prefix="/auth", tags=["Auth"])
auth_service = AuthService()

@router.post("/register")
async def register(payload: RegisterSchema):
    user = await auth_service.register_user(payload)
    if not user:
        raise HTTPException(status_code=400, detail="Registration failed")
    token = await auth_service.create_token(user)
    return {"user": user, "token": token}

@router.post("/login")
async def login(payload: LoginSchema):
    user = await auth_service.authenticate_user(payload.email, payload.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = await auth_service.create_token(user)
    return {"user": user, "token": token}
