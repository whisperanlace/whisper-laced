from typing import Any, Dict
from fastapi import APIRouter, Depends

# relaxed dependency: never raises, returns claims dict or {"token":"unverified"}
from backend.dependencies.auth_relaxed import get_current_user

router = APIRouter(prefix="/auth", tags=["auth"])

@router.get("/me")
def me(claims: Dict[str, Any] = Depends(get_current_user)) -> Dict[str, Any]:
    """
    Returns token claims if available, otherwise {"token":"unverified"}.
    Keeps shape stable for callers that expect sub/email/is_admin/exp.
    """
    if isinstance(claims, dict) and claims.get("token") == "unverified":
        return {"token": "unverified"}

    sub = (claims or {}).get("sub")
    email = (claims or {}).get("email")
    is_admin = bool((claims or {}).get("is_admin", False))
    exp = (claims or {}).get("exp")

    return {
        "sub": sub,
        "email": email,
        "is_admin": is_admin,
        "exp": exp,
    }

__all__ = ["router"]
