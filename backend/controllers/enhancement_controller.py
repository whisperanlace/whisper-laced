from typing import Any, Dict, List
from fastapi import APIRouter
import os, sqlite3

router = APIRouter(prefix="/enhancements", tags=["enhancements"])

def _db_path() -> str:
    url = os.getenv("DATABASE_URL", "").strip()
    if url.startswith("sqlite:///"):
        return os.path.normpath(url[len("sqlite:///"):])
    return os.path.normpath(r"D:/whisper-laced/backend/db.sqlite3")

def _open():
    p = _db_path()
    os.makedirs(os.path.dirname(p), exist_ok=True)
    con = sqlite3.connect(p)
    con.row_factory = sqlite3.Row
    return con

@router.get("/")
def list_enhancements() -> List[Dict[str, Any]]:
    con = _open()
    try:
        cur = con.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='enhancements'")
        if not cur.fetchone():
            return []
        cur.execute("SELECT id, doc_id, instruction, created_at FROM enhancements ORDER BY id DESC LIMIT 100")
        return [dict(r) for r in cur.fetchall()]
    finally:
        con.close()
