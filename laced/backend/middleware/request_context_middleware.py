# middleware/Request_context_middleware.py

from fastapi import Request

async def request_context_middleware(request: Request, call_next):
    # Add any per-request context if needed
    request.state.context = {}
    response = await call_next(request)
    return response
