from __future__ import annotations
import os
from typing import Optional, List, Dict, Any
from types import SimpleNamespace
from fastapi import Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-change-me")
ALGORITHM  = os.getenv("ALGORITHM", "HS256")
ADMIN_EMAILS = {e.strip().lower() for e in os.getenv("ADMIN_EMAILS", "").split(",") if e.strip()}

# Token extractor for docs + convenience (path is only for OpenAPI)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token", auto_error=False)

def _decode_jwt(token: str) -> Dict[str, Any]:
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    # try python-jose first, fall back to pyjwt
    try:
        from jose import jwt as jj
        return jj.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except Exception:
        import jwt as pyjwt
        try:
            return pyjwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        except Exception:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate token")

def _claims_to_principal(claims: Dict[str, Any]) -> SimpleNamespace:
    email = (claims.get("email") or "").lower()
    role  = (claims.get("role") or "").lower() if claims.get("role") else None
    roles = claims.get("roles") or []
    if isinstance(roles, str):
        roles = [roles]
    roles = [str(r).lower() for r in roles]
    # implicit admin if email is allowlisted
    if email and email in ADMIN_EMAILS and "admin" not in roles:
        roles.append("admin")
    return SimpleNamespace(id=str(claims.get("sub") or ""), email=email, role=role, roles=roles, claims=claims)

async def current_principal(request: Request, token: Optional[str] = Depends(oauth2_scheme)):
    # allow either Authorization header OR oauth2_scheme extraction
    if not token:
        auth = request.headers.get("authorization") or request.headers.get("Authorization")
        if auth and auth.lower().startswith("bearer "):
            token = auth.split(" ", 1)[1].strip()
    claims = _decode_jwt(token)
    return _claims_to_principal(claims)

def _require_any(prn: SimpleNamespace, allowed: List[str]):
    r = {*(prn.roles or [])}
    if prn.role: r.add(prn.role)
    if not r.intersection({a.lower() for a in allowed}):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient role")

def require_admin(prn: SimpleNamespace = Depends(current_principal)):
    _require_any(prn, ["admin"])
    return prn

def require_admin_or_moderator(prn: SimpleNamespace = Depends(current_principal)):
    _require_any(prn, ["admin", "moderator"])
    return prn
