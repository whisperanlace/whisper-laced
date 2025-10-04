from typing import Any, Dict, List, Optional
from fastapi import APIRouter, HTTPException, Query, Request
import os, sqlite3

# Try to use PyJWT if present to read sub from token
try:
    import jwt  # PyJWT
except Exception:
    jwt = None

router = APIRouter(prefix="/reports", tags=["reports"])

def _db_path() -> str:
    url = os.getenv("DATABASE_URL", "").strip()
    if url.startswith("sqlite:///"):
        path = url[len("sqlite:///"):]
        return os.path.normpath(path)
    return os.path.normpath(r"D:/whisper-laced/backend/db.sqlite3")

def _open():
    path = _db_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    con = sqlite3.connect(path, timeout=10)
    con.row_factory = sqlite3.Row
    return con

def _user_id_from_token(request: Request) -> int:
    # Best effort parse of "Authorization: Bearer <jwt>"
    auth = request.headers.get("authorization") or request.headers.get("Authorization")
    if not auth or " " not in auth:
        return 1
    scheme, token = auth.split(" ", 1)
    if scheme.lower() != "bearer":
        return 1
    secret = os.getenv("SECRET_KEY", "")
    if not jwt or not secret:
        return 1
    try:
        claims = jwt.decode(token, secret, algorithms=["HS256"])
        sub = claims.get("sub")
        return int(sub) if sub is not None else 1
    except Exception:
        return 1

@router.get("/", response_model=List[Dict[str, Any]])
def list_reports(limit: int = Query(50, ge=1, le=200), offset: int = Query(0, ge=0)):
    con = _open()
    try:
        cur = con.cursor()
        # Use the actual columns present in your DB
        cur.execute(
            "SELECT id, reporter_id, target_type, target_id, reason, details, "
            "status, moderation_case_id, created_at, updated_at, ref_id, topic "
            "FROM reports ORDER BY id DESC LIMIT ? OFFSET ?",
            (limit, offset)
        )
        return [dict(r) for r in cur.fetchall()]
    finally:
        con.close()

@router.post("/", response_model=Dict[str, Any])
def create_report(request: Request, body: Dict[str, Any]):
    # REQUIRED by your schema
    for k in ("reason", "target_type", "target_id"):
        if k not in body:
            raise HTTPException(422, f"Missing field: {k}")

    reporter_id = _user_id_from_token(request)
    reason: str = str(body["reason"])
    target_type: str = str(body["target_type"])
    try:
        target_id: int = int(body["target_id"])
    except Exception:
        raise HTTPException(422, "target_id must be an integer")

    # Optional fields your table also has
    topic: Optional[str] = body.get("topic")
    ref_id: Optional[int] = body.get("ref_id")
    details: Optional[str] = body.get("details")

    con = _open()
    try:
        cur = con.cursor()
        try:
            cur.execute(
                "INSERT INTO reports (reporter_id, target_type, target_id, reason, details, status, created_at, updated_at, ref_id, topic) "
                "VALUES (?,?,?,?,?,'open',datetime('now'),datetime('now'),?,?)",
                (reporter_id, target_type, target_id, reason, details, ref_id, topic)
            )
            rid = cur.lastrowid
            con.commit()
        except Exception as e:
            raise HTTPException(500, f"insert_failed: {type(e).__name__}: {e}")
        cur.execute(
            "SELECT id, reporter_id, target_type, target_id, reason, details, status, moderation_case_id, created_at, updated_at, ref_id, topic "
            "FROM reports WHERE id=?",
            (rid,)
        )
        row = cur.fetchone()
        return dict(row)
    finally:
        con.close()

@router.post("/{report_id}/close", response_model=Dict[str, Any])
def close_report(report_id: int):
    con = _open()
    try:
        cur = con.cursor()
        cur.execute(
            "UPDATE reports SET status='closed', updated_at=datetime('now') WHERE id=?",
            (report_id,)
        )
        con.commit()
        cur.execute(
            "SELECT id, reporter_id, target_type, target_id, reason, details, status, moderation_case_id, created_at, updated_at, ref_id, topic "
            "FROM reports WHERE id=?",
            (report_id,)
        )
        row = cur.fetchone()
        return dict(row) if row else {"id": report_id, "status": "closed"}
    finally:
        con.close()
