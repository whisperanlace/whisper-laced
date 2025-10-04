from __future__ import annotations
import os, sys, json
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

def get_hash_verifier():
    try:
        from passlib.hash import bcrypt as pl_bcrypt
        def verify(p, h): 
            try: return pl_bcrypt.verify(p, h)
            except Exception: return False
        return "passlib.bcrypt", verify
    except Exception:
        pass
    try:
        import bcrypt
        def verify(p, h):
            try: return bcrypt.checkpw(p.encode("utf-8"), h.encode("utf-8"))
            except Exception: return False
        return "bcrypt", verify
    except Exception:
        pass
    return "none", lambda p,h: False

def show(email: str, password: str):
    from backend.models import User
    db = session()
    try:
        u = db.query(User).filter(User.email == email).first()
        if not u:
            print(json.dumps({"exists": False}))
            return
        fields = {}
        for k in ("hashed_password","password_hash","password","role","roles","username","api_key"):
            if hasattr(u, k):
                v = getattr(u, k)
                if isinstance(v, str):
                    fields[k] = (len(v), v[:8] + "..." if len(v)>8 else v)
                else:
                    fields[k] = str(v)
        which, verify = get_hash_verifier()
        hashed = None
        for name in ("hashed_password","password_hash","password"):
            if hasattr(u, name):
                hv = getattr(u, name)
                if isinstance(hv, str) and hv:
                    hashed = hv; used = name; break
        ok = verify(password, hashed) if hashed else False
        print(json.dumps({
            "exists": True,
            "id": getattr(u,"id",None),
            "email": getattr(u,"email",None),
            "password_field": used if hashed else None,
            "verifier": which,
            "verify_ok": ok,
            "fields": fields,
        }, default=str))
    finally:
        db.close()

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--email", required=True)
    ap.add_argument("--password", required=True)
    a = ap.parse_args()
    show(a.email, a.password)

