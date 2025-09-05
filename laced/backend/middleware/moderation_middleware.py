# middleware/Moderation_middleware.py

from fastapi import Request, HTTPException

async def moderation_middleware(request: Request, call_next):
    user = getattr(request.state, "user", None)
    if not user or not user.get("is_moderator", False):
        raise HTTPException(status_code=403, detail="Moderator access required")
    response = await call_next(request)
    return response
