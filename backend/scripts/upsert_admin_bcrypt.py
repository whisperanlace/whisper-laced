from __future__ import annotations
import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

def session():
    try:
        from backend.db import SessionLocal
        return SessionLocal()
    except Exception:
        from backend.db import engine
        from sqlalchemy.orm import sessionmaker
        return sessionmaker(bind=engine, autoflush=False, autocommit=False)()

def bcrypt_hash(pw: str) -> str:
    try:
        from passlib.hash import bcrypt
        return bcrypt.hash(pw)
    except Exception:
        pass
    try:
        import bcrypt as _b
        return _b.hashpw(pw.encode("utf-8"), _b.gensalt()).decode("utf-8")
    except Exception as e:
        raise RuntimeError("Install a hasher: pip install 'passlib[bcrypt]' OR pip install bcrypt") from e

def upsert_admin(email: str, password: str):
    from backend.models import User
    db = session()
    try:
        u = db.query(User).filter(User.email == email).first()
        hashed = bcrypt_hash(password)

        if u is None:
            # Build a new instance WITHOUT flushing until hashed is set
            u = User()
            # minimal required fields first
            if hasattr(u, "email"): setattr(u, "email", email)
            if hasattr(u, "username") and not getattr(u, "username", None):
                setattr(u, "username", email.split("@")[0])
            # set the *required* password column BEFORE any flush
            set_pw = False
            for field in ("hashed_password", "password_hash", "password"):
                if hasattr(u, field):
                    setattr(u, field, hashed)
                    set_pw = True
                    break
            if not set_pw:
                raise RuntimeError("User model has no password column among: hashed_password/password_hash/password")

            # set role(s) to admin if present
            if hasattr(u, "role"):
                setattr(u, "role", "admin")
            if hasattr(u, "roles"):
                try:
                    seq = list(getattr(u, "roles"))
                except Exception:
                    seq = []
                if "admin" not in [str(x).lower() for x in seq]:
                    seq.append("admin")
                    setattr(u, "roles", seq)

            db.add(u)
            # now safe to flush/commit
            db.commit()
            db.refresh(u)
        else:
            # Existing user: ensure password and admin role
            updated = False
            pw_field = None
            for field in ("hashed_password", "password_hash", "password"):
                if hasattr(u, field):
                    pw_field = field
                    break
            if pw_field:
                if not getattr(u, pw_field, None):
                    setattr(u, pw_field, hashed)
                    updated = True
            # role promotion
            if hasattr(u, "role") and getattr(u, "role", None) != "admin":
                setattr(u, "role", "admin"); updated = True
            if hasattr(u, "roles"):
                try:
                    seq = list(getattr(u, "roles"))
                except Exception:
                    seq = []
                if "admin" not in [str(x).lower() for x in seq]:
                    seq.append("admin")
                    setattr(u, "roles", seq)
                    updated = True
            if updated:
                db.add(u)
                db.commit()
                db.refresh(u)

        print({"id": getattr(u, "id", None), "email": getattr(u, "email", None)})
    finally:
        db.close()

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--email", required=True)
    ap.add_argument("--password", required=True)
    args = ap.parse_args()
    upsert_admin(args.email, args.password)

