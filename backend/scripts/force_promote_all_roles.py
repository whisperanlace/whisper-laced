from __future__ import annotations
import os, sys, json
sys.path.insert(0, r"D:\whisper-laced")

from sqlalchemy import text
from backend.db import SessionLocal
from backend.models import User

EMAIL = "whisperandlaced@gmail.com"

def go():
    db = SessionLocal()
    try:
        u = db.query(User).filter(User.email==EMAIL).first()
        if not u:
            return {"ok": False, "error": "user not found"}

        changed = False
        # common fields various codebases check:
        if hasattr(u, "role") and getattr(u, "role") != "ADMIN":
            u.role = "ADMIN"; changed = True
        if hasattr(u, "roles"):
            # include upper + lower variants
            try:
                roles = list(u.roles or [])
            except Exception:
                roles = []
            wanted = {"ADMIN","MODERATOR","admin","moderator"}
            if isinstance(roles, (list, tuple, set)):
                have = set(str(r) for r in roles)
                miss = [r for r in wanted if r not in have]
                if miss:
                    try:
                        u.roles = list(have | set(miss))
                        changed = True
                    except Exception:
                        pass
        for flag in ("is_admin","is_staff","is_moderator","is_superuser"):
            if hasattr(u, flag) and not getattr(u, flag):
                try:
                    setattr(u, flag, True)
                    changed = True
                except Exception:
                    pass

        if changed:
            db.add(u); db.commit(); db.refresh(u)

        row = db.execute(text("SELECT * FROM users WHERE email=:e"), {"e": EMAIL}).mappings().first()
        return {"ok": True, "id": u.id, "email": EMAIL, "changed": changed, "row": dict(row) if row else None}
    finally:
        db.close()

if __name__ == "__main__":
    print(json.dumps(go()))

