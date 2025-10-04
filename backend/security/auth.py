from __future__ import annotations
import os
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from starlette.status import HTTP_401_UNAUTHORIZED

# If BEARER_TOKEN is unset/empty, auth is disabled (allow all).
_BEARER = os.getenv("BEARER_TOKEN", "").strip()
_scheme = HTTPBearer(auto_error=False)

def auth_bearer(creds: HTTPAuthorizationCredentials = Depends(_scheme)) -> None:
    if not _BEARER:  # auth disabled
        return
    if creds is None or creds.scheme.lower() != "bearer" or creds.credentials != _BEARER:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Unauthorized")