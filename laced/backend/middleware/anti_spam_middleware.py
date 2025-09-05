# middleware/Anti_spam_middleware.py

from fastapi import Request, HTTPException

REQUEST_HISTORY = {}

async def anti_spam_middleware(request: Request, call_next):
    user_id = getattr(request.state.user, "id", None)
    if user_id:
        history = REQUEST_HISTORY.get(user_id, [])
        if len(history) >= 10:
            raise HTTPException(status_code=429, detail="Spam detected")
        history.append(request.url.path)
        REQUEST_HISTORY[user_id] = history[-10:]
    response = await call_next(request)
    return response
