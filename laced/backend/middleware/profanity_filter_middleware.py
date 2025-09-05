# middleware/Profanity_filter_middleware.py

from fastapi import Request, HTTPException

PROFANITY_LIST = ["badword1", "badword2"]

async def profanity_filter_middleware(request: Request, call_next):
    body = await request.body()
    content = body.decode() if body else ""
    if any(word in content.lower() for word in PROFANITY_LIST):
        raise HTTPException(status_code=400, detail="Profanity detected")
    response = await call_next(request)
    return response
