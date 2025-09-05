# middleware/Role_middleware.py

from fastapi import Request, HTTPException

def role_required(allowed_roles):
    async def middleware(request: Request, call_next):
        user = getattr(request.state, "user", None)
        if not user or user.get("role") not in allowed_roles:
            raise HTTPException(status_code=403, detail="Forbidden")
        response = await call_next(request)
        return response
    return middleware
