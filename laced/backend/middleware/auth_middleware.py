# middleware/Auth_middleware.py

from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Callable
import jwt
from starlette.responses import JSONResponse

security = HTTPBearer()

SECRET_KEY = "YOUR_SECRET_KEY"

async def auth_middleware(request: Request, call_next: Callable):
    try:
        credentials: HTTPAuthorizationCredentials = await security(request)
        token = credentials.credentials
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        request.state.user = payload
    except Exception:
        raise HTTPException(status_code=401, detail="Unauthorized")
    response = await call_next(request)
    return response
