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

def promote_admin(db, u):
    changed = False
    if hasattr(u, "role"):
        if getattr(u, "role", None) != "admin":
            setattr(u, "role", "admin"); changed = True
    if hasattr(u, "roles"):
        try:
            seq = list(getattr(u, "roles"))
        except Exception:
            seq = []
        low = [str(x).lower() for x in seq]
        if "admin" not in low:
            seq.append("admin"); setattr(u, "roles", seq); changed = True
    if changed: db.add(u)
    return changed

def find_user(db, email):
    from backend.models import User
    return db.query(User).filter(User.email == email).first()

def try_import_user_schema():
    # Try common schema module names and class names
    schema_mod_candidates = [
        "backend.schemas.user_schema",
        "backend.schemas.users",
        "backend.schemas.user",
        "backend.schemas",
    ]
    class_candidates = ["UserCreate","UserInCreate","UserRegister","RegisterRequest","UserSignup","UserCreateSchema"]
    for mod in schema_mod_candidates:
        try:
            m = __import__(mod, fromlist=["*"])
        except Exception:
            continue
        for cls in class_candidates:
            t = getattr(m, cls, None)
            if t:
                return t, f"{mod}.{cls}"
    return None, None

def try_user_service_create(db, email, password):
    # Prefer service API so hashing matches your production code
    try:
        from backend.services import user_service
    except Exception as e:
        return None, f"user_service import failed: {e}"

    schema_type, schema_name = try_import_user_schema()
    obj_variants = []
    if schema_type:
        # Build schema instance with common fields
        for fields in (
            dict(email=email, password=password, is_active=True),
            dict(email=email, password=password),
            dict(username=email.split("@")[0], email=email, password=password, is_active=True),
            dict(username=email.split("@")[0], email=email, password=password),
        ):
            try:
                obj = schema_type(**fields)
                obj_variants.append(("schema", obj, fields))
            except Exception:
                pass

    # Also try plain dict payload
    obj_variants += [
        ("dict", dict(email=email, password=password, is_active=True), None),
        ("dict", dict(email=email, password=password), None),
    ]

    func_candidates = [
        "register",
        "create_user",
        "create",
        "create_user_with_password",
        "signup",
        "create_with_password",
    ]

    # Try function(obj=..., db=...), function(db=..., obj=...), function(db=..., email=..., password=...)
    for fname in func_candidates:
        fn = getattr(user_service, fname, None)
        if not fn:
            continue
        for kind, payload, raw in obj_variants:
            try:
                # try as obj argument name variants
                for argname in ("user_in","user","data","payload","schema"):
                    try:
                        u = fn(db=db, **{argname: payload})
                        if u: return u, f"user_service.{fname}({argname}=..., db=...) via {schema_name or kind}"
                    except TypeError:
                        continue
                # try named fields
                try:
                    u = fn(db=db, email=email, password=password)
                    if u: return u, f"user_service.{fname}(email,password) direct"
                except TypeError:
                    pass
            except Exception:
                continue
    return None, "no matching service create function worked"

def provision(email, password):
    db = session()
    try:
        u = find_user(db, email)
        created_via = None
        if u is None:
            u, created_via = try_user_service_create(db, email, password)
            if u is None:
                # Last resort: bare User(); won't set password (so token may still fail until you register properly)
                from backend.models import User
                u = User()
                if hasattr(u, "email"): setattr(u, "email", email)
                if hasattr(u, "username") and not getattr(u, "username", None):
                    setattr(u, "username", email.split("@")[0])
                if hasattr(u, "is_active"): setattr(u, "is_active", True)
                db.add(u); db.flush()
                created_via = "bare User() fallback (no password set)"
        changed = promote_admin(db, u)
        db.commit(); db.refresh(u)
        return {"id": getattr(u, "id", None), "email": getattr(u, "email", None), "created_via": created_via, "promoted": changed}
    finally:
        db.close()

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--email", required=True)
    ap.add_argument("--password", required=True)
    args = ap.parse_args()
    print(json.dumps(provision(args.email, args.password)))

