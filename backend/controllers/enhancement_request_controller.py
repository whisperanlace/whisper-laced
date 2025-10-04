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

def _ensure_schema(con: sqlite3.Connection):
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS enhancement_requests(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        doc_id INTEGER NOT NULL,
        instruction TEXT NOT NULL,
        created_at TEXT DEFAULT (datetime('now'))
    );""")
    con.commit()

@router.get("/")
def list_enhancements() -> List[Dict[str, Any]]:
    con = _open()
    try:
        _ensure_schema(con)
        cur = con.cursor()
        cur.execute("""SELECT id, doc_id, instruction, created_at
                       FROM enhancement_requests
                       ORDER BY id DESC LIMIT 100""")
        return [dict(r) for r in cur.fetchall()]
    finally:
        con.close()
