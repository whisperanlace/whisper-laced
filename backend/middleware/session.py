import secrets
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp

COOKIE = "sid"

class SessionMiddlewareLite(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp):
        super().__init__(app)

    async def dispatch(self, request, call_next):
        sid = request.cookies.get(COOKIE)
        if not sid:
            sid = secrets.token_hex(16)
            request.state.new_sid = sid
        request.state.session_id = sid
        response = await call_next(request)
        if getattr(request.state, "new_sid", None):
            response.set_cookie(COOKIE, sid, httponly=True, samesite="lax", max_age=60*60*24*7)
        return response
