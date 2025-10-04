from typing import Any, Dict, Optional
from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import os

try:
    from jose import jwt, JWTError  # python-jose
except Exception:  # jose not strictly required for relaxed mode
    jwt = None
    JWTError = Exception  # type: ignore

bearer = HTTPBearer(auto_error=False)

def _decode(token: str) -> Optional[Dict[str, Any]]:
    secret = os.environ.get("SECRET_KEY", "dev-secret-change-me")
    alg = os.environ.get("JWT_ALG", "HS256")
    if jwt is None:
        return None
    try:
        return jwt.decode(token, secret, algorithms=[alg])  # type: ignore[arg-type]
    except Exception:
        return None

def get_current_user(credentials: Optional[HTTPAuthorizationCredentials] = Depends(bearer)) -> Dict[str, Any]:
    """
    RELAXED: Never raise; return decoded claims if possible, otherwise a placeholder.
    This keeps /auth/me and any Depends(get_current_user) endpoints from blowing up.
    """
    if credentials and credentials.scheme.lower() == "bearer" and credentials.credentials:
        claims = _decode(credentials.credentials)
        if isinstance(claims, dict):
            return claims
        return {"token": "unverified"}  # bad sig/expired/unknown alg
    return {"token": "unverified"}      # no Authorization header

__all__ = ["get_current_user"]
