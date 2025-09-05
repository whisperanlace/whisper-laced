# middleware/error_middleware.py

from fastapi import Request
from fastapi.responses import JSONResponse

async def error_middleware(request: Request, call_next):
    try:
        response = await call_next(request)
        if response.status_code >= 400:
            return JSONResponse(
                status_code=response.status_code,
                content={"detail": getattr(response, "body", "Error")},
            )
        return response
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"detail": str(e)},
        )
