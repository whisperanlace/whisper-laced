# middleware/Lora_middleware.py

from fastapi import Request, HTTPException

async def lora_middleware(request: Request, call_next):
    user = getattr(request.state, "user", None)
    if not user or not user.get("can_upload_lora", False):
        raise HTTPException(status_code=403, detail="LoRA access denied")
    response = await call_next(request)
    return response
