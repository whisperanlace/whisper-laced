# middleware/Editor_middleware.py

from fastapi import Request, HTTPException

async def editor_middleware(request: Request, call_next):
    user = getattr(request.state, "user", None)
    if not user or not user.get("can_use_editor", False):
        raise HTTPException(status_code=403, detail="Editor access denied")
    response = await call_next(request)
    return response
