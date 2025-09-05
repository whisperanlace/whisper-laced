# middleware/Signature_middleware.py

from fastapi import Request, HTTPException
import hmac
import hashlib

SECRET_KEY = b"YOUR_SECRET_KEY"

async def signature_middleware(request: Request, call_next):
    signature = request.headers.get("X-Signature")
    body = await request.body()
    computed = hmac.new(SECRET_KEY, body, hashlib.sha256).hexdigest()
    if not signature or not hmac.compare_digest(signature, computed):
        raise HTTPException(status_code=403, detail="Invalid signature")
    response = await call_next(request)
    return response
