# middleware/User_middleware.py

from fastapi import Request, HTTPException

async def user_middleware(request: Request, call_next):
    if not hasattr(request.state, "user"):
        raise HTTPException(status_code=401, detail="User not authenticated")
    response = await call_next(request)
    return response
