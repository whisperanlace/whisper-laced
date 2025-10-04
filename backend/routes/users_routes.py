from fastapi import APIRouter, Depends
from backend.dependencies.auth import get_current_user
from backend.schemas.auth import UserOut

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me", response_model=UserOut)
def me(current: UserOut = Depends(get_current_user)):
    return current
