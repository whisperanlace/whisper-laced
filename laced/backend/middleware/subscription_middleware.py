# middleware/Subscription_middleware.py

from fastapi import Request, HTTPException

async def subscription_middleware(request: Request, call_next):
    user = getattr(request.state, "user", None)
    if not user or not user.get("subscription_active", False):
        raise HTTPException(status_code=402, detail="Subscription required")
    response = await call_next(request)
    return response
