from typing import Any, Dict, List
from fastapi import APIRouter, HTTPException
import os, sqlite3

router = APIRouter(prefix="/editor", tags=["editor"])

# ---------- DB helpers ----------
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
    # editor_documents
    cur.execute("""CREATE TABLE IF NOT EXISTS editor_documents(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        created_at TEXT DEFAULT (datetime('now'))
    );""")
    # editor_versions
    cur.execute("""CREATE TABLE IF NOT EXISTS editor_versions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        doc_id INTEGER NOT NULL,
        version INTEGER NOT NULL,
        body TEXT NOT NULL,
        created_at TEXT DEFAULT (datetime('now')),
        UNIQUE(doc_id, version)
    );""")
    con.commit()

# ---------- routes ----------
@router.get("/ping")
def ping():
    return {"ok": True, "router": "editor", "db": _db_path()}

@router.post("/documents")
def create_document(body: Dict[str, Any]) -> Dict[str, Any]:
    title = (body or {}).get("title")
    text  = (body or {}).get("body")
    if not title or not text:
        raise HTTPException(422, "title and body are required")
    con = _open()
    try:
        _ensure_schema(con)
        cur = con.cursor()
        cur.execute("INSERT INTO editor_documents(title) VALUES(?)", (title,))
        doc_id = cur.lastrowid
        # v1
        cur.execute("INSERT INTO editor_versions(doc_id, version, body) VALUES(?,?,?)",
                    (doc_id, 1, text))
        con.commit()
        return {"id": doc_id, "title": title, "body": text, "version": 1}
    finally:
        con.close()

@router.get("/documents/{doc_id}")
def read_document(doc_id: int) -> Dict[str, Any]:
    con = _open()
    try:
        _ensure_schema(con)
        cur = con.cursor()
        cur.execute("SELECT id, title, created_at FROM editor_documents WHERE id=?", (doc_id,))
        doc = cur.fetchone()
        if not doc:
            raise HTTPException(404, "document not found")
        cur.execute("""SELECT version, body, created_at
                       FROM editor_versions
                       WHERE doc_id=? ORDER BY version DESC LIMIT 1""", (doc_id,))
        ver = cur.fetchone()
        if not ver:
            raise HTTPException(500, "document has no versions")
        return {
            "id": doc["id"], "title": doc["title"], "created_at": doc["created_at"],
            "version": ver["version"], "body": ver["body"], "version_created_at": ver["created_at"],
        }
    finally:
        con.close()

@router.get("/documents/{doc_id}/versions")
def list_versions(doc_id: int) -> List[Dict[str, Any]]:
    con = _open()
    try:
        _ensure_schema(con)
        cur = con.cursor()
        cur.execute("""SELECT version, body, created_at
                       FROM editor_versions
                       WHERE doc_id=? ORDER BY version ASC""", (doc_id,))
        return [dict(r) for r in cur.fetchall()]
    finally:
        con.close()

@router.post("/documents/{doc_id}/enhance")
def enhance_document(doc_id: int, body: Dict[str, Any]) -> Dict[str, Any]:
    instruction = (body or {}).get("instruction")
    if not instruction:
        raise HTTPException(422, "instruction is required")
    con = _open()
    try:
        _ensure_schema(con)
        cur = con.cursor()
        # get latest version + body
        cur.execute("""SELECT version, body FROM editor_versions
                       WHERE doc_id=? ORDER BY version DESC LIMIT 1""", (doc_id,))
        last = cur.fetchone()
        if not last:
            raise HTTPException(404, "document not found")
        last_v = int(last["version"])
        last_body = last["body"]
        # naive “enhancement”: trim + ensure final punctuation (placeholder)
        new_body = (last_body or "").strip()
        if new_body and new_body[-1] not in ".!?":
            new_body = new_body + "."
        new_v = last_v + 1
        cur.execute("INSERT INTO editor_versions(doc_id, version, body) VALUES(?,?,?)",
                    (doc_id, new_v, new_body))
        # also log enhancement in enhancement_requests if that table exists
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='enhancement_requests'")
        if cur.fetchone():
            cur.execute("""INSERT INTO enhancement_requests(doc_id, instruction)
                           VALUES(?,?)""", (doc_id, instruction))
        con.commit()
        return {"doc_id": doc_id, "version": new_v, "body": new_body, "instruction": instruction}
    finally:
        con.close()
