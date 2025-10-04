from __future__ import annotations
import argparse, sys
from backend.db import SessionLocal
from backend.models import User

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--email", required=True)
    args = ap.parse_args()

    db = SessionLocal()
    try:
        u = db.query(User).filter(User.email==args.email.lower()).first()
        if not u:
            print({"ok": False, "error": "user not found"}); return
        # ensure the flag exists; many schemas already have it
        if not hasattr(u, "is_admin"):
            print({"ok": False, "error": "user model missing is_admin"}) ; return
        u.is_admin = True
        # optional: populate role/roles if your model has them
        if hasattr(u, "role") and not getattr(u, "role"):
            u.role = "admin"
        if hasattr(u, "roles"):
            try:
                roles = set((u.roles or []))
                roles.add("admin")
                u.roles = list(roles)
            except Exception:
                pass
        db.add(u); db.commit(); db.refresh(u)
        print({"ok": True, "id": u.id, "email": u.email, "is_admin": getattr(u, "is_admin", None), "role": getattr(u, "role", None)})
    finally:
        db.close()

if __name__ == "__main__":
    main()

