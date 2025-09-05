# middleware/Report_middleware.py

from fastapi import Request, HTTPException

async def report_middleware(request: Request, call_next):
    user = getattr(request.state, "user", None)
    if not user or not user.get("can_report", False):
        raise HTTPException(status_code=403, detail="Reporting not allowed")
    response = await call_next(request)
    return response
