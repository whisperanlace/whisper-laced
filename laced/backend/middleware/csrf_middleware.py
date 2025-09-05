# middleware/Csrf_middleware.py

from fastapi import Request, HTTPException

async def csrf_middleware(request: Request, call_next):
    if request.method in ["POST", "PUT", "DELETE"]:
        token = request.headers.get("X-CSRF-Token")
        if not token or token != "VALID_CSRF_TOKEN":
            raise HTTPException(status_code=403, detail="CSRF token invalid")
    response = await call_next(request)
    return response
