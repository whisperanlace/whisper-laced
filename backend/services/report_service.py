from typing import Any, Dict, List
from sqlalchemy.orm import Session

def _ensure_reports_schema(db: Session) -> None:
    # Works even if the table exists with fewer/different columns
    conn = db.connection().connection  # SQLAlchemy -> sqlite3 connection
    cur = conn.cursor()
    cur.execute("PRAGMA table_info(reports)")
    cols = {row[1] for row in cur.fetchall()}

    # If table missing entirely, create it
    if not cols:
        cur.execute("""
            CREATE TABLE reports(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ref_id INTEGER,
                topic TEXT,
                reason TEXT,
                status TEXT DEFAULT 'open',
                created_at TEXT DEFAULT (datetime('now'))
            )
        """)
        conn.commit()
        return

    # Add any missing columns
    desired = {
        "ref_id": "INTEGER",
        "topic": "TEXT",
        "reason": "TEXT",
        "status": "TEXT",
        "created_at": "TEXT"
    }
    for name, ddl in desired.items():
        if name not in cols:
            cur.execute(f"ALTER TABLE reports ADD COLUMN {name} {ddl}")
    conn.commit()

def create_report(db: Session, payload: Dict[str, Any]) -> Dict[str, Any]:
    _ensure_reports_schema(db)
    conn = db.connection().connection
    cur = conn.cursor()
    topic  = payload.get("topic")
    reason = payload.get("reason")
    ref_id = payload.get("ref_id")
    cur.execute(
        "INSERT INTO reports(topic, reason, ref_id, status, created_at) VALUES(?,?,?,?,datetime('now'))",
        (topic, reason, ref_id, "open")
    )
    conn.commit()
    rid = cur.lastrowid
    cur.execute("SELECT id, topic, reason, ref_id, status, created_at FROM reports WHERE id=?", (rid,))
    row = cur.fetchone()
    return {
        "id": row[0], "topic": row[1], "reason": row[2],
        "ref_id": row[3], "status": row[4], "created_at": row[5]
    }

def list_reports(db: Session, limit: int = 50, offset: int = 0) -> List[Dict[str, Any]]:
    _ensure_reports_schema(db)
    conn = db.connection().connection
    cur = conn.cursor()
    cur.execute(
        "SELECT id, topic, reason, ref_id, status, created_at FROM reports ORDER BY id DESC LIMIT ? OFFSET ?",
        (limit, offset)
    )
    return [
        {"id": r[0], "topic": r[1], "reason": r[2], "ref_id": r[3], "status": r[4], "created_at": r[5]}
        for r in cur.fetchall()
    ]

def close_report(db: Session, report_id: int) -> Dict[str, Any]:
    _ensure_reports_schema(db)
    conn = db.connection().connection
    cur = conn.cursor()
    cur.execute("UPDATE reports SET status='closed' WHERE id=?", (report_id,))
    conn.commit()
    cur.execute("SELECT id, topic, reason, ref_id, status, created_at FROM reports WHERE id=?", (report_id,))
    row = cur.fetchone()
    if not row:
        return {"id": report_id, "status": "closed"}
    return {
        "id": row[0], "topic": row[1], "reason": row[2],
        "ref_id": row[3], "status": row[4], "created_at": row[5]
    }
