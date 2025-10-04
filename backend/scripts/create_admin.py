from __future__ import annotations
import os, sys, argparse

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

def get_session():
    try:
        from backend.db import SessionLocal  # preferred
        return SessionLocal()
    except Exception:
        from sqlalchemy.orm import sessionmaker
        from backend.db import engine
        return sessionmaker(bind=engine, autoflush=False, autocommit=False)()

def get_password_hash_fn():
    try:
        from backend.core import auth
        if hasattr(auth, "get_password_hash"):
            return auth.get_password_hash
    except Exception:
        pass
    raise RuntimeError("Missing password hasher (expected backend.core.auth.get_password_hash)")

def ensure_admin(email: str, password: str):
    from sqlalchemy import inspect
    from backend.dependencies.roles import UserRole

    db = get_session()
    try:
        # import User model
        try:
            from backend.models import User
        except Exception as e:
            raise RuntimeError(f"Could not import backend.models.user: {e}")

        # find existing
        user = db.query(User).filter(getattr(User, "email")==email).first()

        # create if missing
        if user is None:
            user = User()
            if hasattr(user, "email"):
                setattr(user, "email", email)
            if hasattr(user, "username") and not getattr(user, "username", None):
                setattr(user, "username", email.split("@")[0])
            if hasattr(user, "is_active"):
                setattr(user, "is_active", True)
            db.add(user)

        # set password (prefer hashed_password -> password_hash -> password)
        hasher = get_password_hash_fn()
        hashed = hasher(password)
        if hasattr(user, "hashed_password"):
            setattr(user, "hashed_password", hashed)
        elif hasattr(user, "password_hash"):
            setattr(user, "password_hash", hashed)
        elif hasattr(user, "password"):
            # if your model stores plaintext (not recommended) we still set hashed
            setattr(user, "password", hashed)
        else:
            raise RuntimeError("User model has no password field (expected hashed_password/password_hash/password)")

        # set role to admin
        if hasattr(user, "role"):
            setattr(user, "role", "admin")
        elif hasattr(user, "roles"):
            val = getattr(user, "roles")
            try:
                # support list/tuple/set
                seq = list(val) if isinstance(val, (list, tuple, set)) else []
            except Exception:
                seq = []
            if "admin" not in [str(x).lower() for x in seq]:
                seq.append("admin")
            setattr(user, "roles", seq)

        db.commit()
        db.refresh(user)
        return {"id": getattr(user, "id", None), "email": getattr(user, "email", None)}
    finally:
        db.close()

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--email", required=True)
    ap.add_argument("--password", required=True)
    args = ap.parse_args()
    out = ensure_admin(args.email, args.password)
    print(out)

