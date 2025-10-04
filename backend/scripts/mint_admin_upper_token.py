from __future__ import annotations
import os, sys, json, datetime as dt
sys.path.insert(0, r"D:\whisper-laced")

EMAIL = "whisperandlaced@gmail.com"
UID   = "1"  # from your upsert

claims = {
    "sub": UID,                     # id
    "email": EMAIL,
    "role": "ADMIN",
    "roles": ["ADMIN","MODERATOR"],
    "scope": "admin",               # some guards use single string "scope"
    "scopes": ["admin","moderation"],
    "permissions": ["ADMIN","MODERATOR"],
    "is_admin": True,
    "is_staff": True,
    "is_moderator": True,
    "is_superuser": True,
    "exp": dt.datetime.utcnow() + dt.timedelta(minutes=60),
}

def make_token(c):
    try:
        from backend.core import auth
        if hasattr(auth, "create_access_token"):
            return auth.create_access_token(c)
    except Exception:
        pass
    secret = os.getenv("SECRET_KEY","dev-secret-change-me")
    alg    = os.getenv("ALGORITHM","HS256")
    try:
        from jose import jwt as jj
        return jj.encode(c, secret, algorithm=alg)
    except Exception:
        import jwt as pj
        t = pj.encode(c, secret, algorithm=alg)
        return t.decode() if isinstance(t, bytes) else t

print(json.dumps({"access_token": make_token(claims)}))
