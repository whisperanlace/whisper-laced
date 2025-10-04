from __future__ import annotations
import os, sys, json
sys.path.insert(0, r"D:\whisper-laced")

from sqlalchemy import inspect, text
from backend.db import SessionLocal
from backend.models import User

EMAIL = "whisperandlaced@gmail.com"

def promote():
    db = SessionLocal()
    try:
        u = db.query(User).filter(User.email == EMAIL).first()
        if not u:
            return {"ok": False, "error": "User not found"}
        changed = False

        # set any/all role fields this model might have
        if hasattr(u, "role") and getattr(u, "role") != "admin":
            u.role = "admin"; changed = True
        if hasattr(u, "roles"):
            try:
                roles = list(u.roles or [])
            except Exception:
                roles = []
            low = [str(r).lower() for r in roles]
            if "admin" not in low:
                roles.append("admin")
                try:
                    u.roles = roles
                except Exception:
                    pass
                changed = True
        if hasattr(u, "is_admin") and not getattr(u, "is_admin"):
            try:
                u.is_admin = True
                changed = True
            except Exception:
                pass
        if hasattr(u, "is_moderator") and not getattr(u, "is_moderator"):
            try:
                u.is_moderator = True
                changed = True
            except Exception:
                pass

        if changed:
            db.add(u); db.commit(); db.refresh(u)

        # reflect DB columns + values for visibility
        insp = inspect(db.bind)
        cols = [c["name"] for c in db.execute(text("PRAGMA table_info(users)")).mappings()]
        row = db.execute(text("SELECT * FROM users WHERE email=:e"), {"e": EMAIL}).mappings().first()
        return {"ok": True, "id": u.id, "email": EMAIL, "changed": changed, "columns": cols, "row": dict(row) if row else None}
    finally:
        db.close()

if __name__ == "__main__":
    print(json.dumps(promote()))

