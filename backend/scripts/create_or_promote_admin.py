from __future__ import annotations
import os, sys, argparse
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

def get_session():
    try:
        from backend.db import SessionLocal
        return SessionLocal()
    except Exception:
        from sqlalchemy.orm import sessionmaker
        from backend.db import engine
        return sessionmaker(bind=engine, autoflush=False, autocommit=False)()

def find_user(db, email):
    from backend.models import User
    return db.query(User).filter(User.email == email).first()

def create_via_service(db, email: str, password: str):
    """
    Try several common user_service APIs so we reuse YOUR hashing:
      - user_service.register(db, email, password, **extras)
      - user_service.create_user(db, email, password, **extras)
      - user_service.create(db, email, password, **extras)
      - user_service.create_user_with_password(...)
    Returns user or None.
    """
    try:
        from backend.services import user_service
    except Exception:
        return None

    extras = {"is_active": True}
    funcs = [
        ("register", ("db","email","password")),
        ("create_user", ("db","email","password")),
        ("create", ("db","email","password")),
        ("create_user_with_password", ("db","email","password")),
    ]

    for name, _ in funcs:
        if hasattr(user_service, name):
            fn = getattr(user_service, name)
            try:
                # try common signatures
                user = fn(db=db, email=email, password=password, **extras)
                if user is None:
                    # some services return (user, token) or dict
                    continue
                return user
            except TypeError:
                # fallback with fewer kwargs
                try:
                    user = fn(db=db, email=email, password=password)
                    if user: return user
                except Exception:
                    pass
            except Exception:
                pass
    return None

def set_role_admin(db, user):
    # Works if your model has role (str) or roles (list)
    if hasattr(user, "role"):
        setattr(user, "role", "admin")
    if hasattr(user, "roles"):
        val = getattr(user, "roles")
        try:
            seq = list(val) if isinstance(val, (list, tuple, set)) else []
        except Exception:
            seq = []
        if "admin" not in [str(x).lower() for x in seq]:
            seq.append("admin")
        setattr(user, "roles", seq)
    db.add(user)

def upsert_admin(email: str, password: str):
    db = get_session()
    try:
        u = find_user(db, email)
        if u is None:
            # Create THROUGH your service to get correct hashing
            u = create_via_service(db, email, password)
            if u is None:
                # Final fallback: try a very generic model init path.
                from backend.models import User
                u = User(email=email, is_active=True)
                # We don't set password here — your auth won’t validate it without service/hasher.
                # This path is only to ensure row exists so you can fix via normal register later.
                db.add(u)
                db.flush()
        # Promote to admin
        set_role_admin(db, u)
        db.commit()
        db.refresh(u)
        return {"id": getattr(u, "id", None), "email": getattr(u, "email", None)}
    finally:
        db.close()

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--email", required=True)
    ap.add_argument("--password", required=True)
    args = ap.parse_args()
    print(upsert_admin(args.email, args.password))

