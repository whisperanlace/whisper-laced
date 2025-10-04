from __future__ import annotations
from pathlib import Path
from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import FileResponse
from starlette.status import HTTP_404_NOT_FOUND, HTTP_403_FORBIDDEN
from backend.config import settings
from backend.security.signer import verify

router = APIRouter(prefix="/files", tags=["files"])

ROOT = Path(settings.OUTPUT_DIR).resolve()

@router.get("/{name}")
def get_file(name: str, exp: int = Query(...), sig: str = Query(...)):
    # Normalize and prevent traversal
    p = (ROOT / name).resolve()
    if ROOT not in p.parents and p != ROOT:
        raise HTTPException(HTTP_403_FORBIDDEN, "Forbidden")
    if not verify(f"/files/{name}", exp, sig):
        raise HTTPException(HTTP_403_FORBIDDEN, "Invalid or expired signature")
    if not p.exists() or not p.is_file():
        raise HTTPException(HTTP_404_NOT_FOUND, "Not found")
    return FileResponse(str(p), filename=p.name)