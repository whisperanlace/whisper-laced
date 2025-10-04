from __future__ import annotations
import os, sys, json, datetime as dt
sys.path.insert(0, r"D:\whisper-laced")

EMAIL = "whisperandlaced@gmail.com"
UID   = "1"  # we just created id=1 above

claims = {
    "sub": UID,                    # user id
    "email": EMAIL,
    "role": "admin",
    "roles": ["admin", "moderator"],
    "scopes": ["admin"],           # for OAuth2 scopes-based guards
    "permissions": ["admin"],      # some apps check this
    "is_admin": True,
    "exp": dt.datetime.utcnow() + dt.timedelta(minutes=60),
}

def make_token(c):
    # prefer app's JWT function
    try:
        from backend.core import auth
        if hasattr(auth, "create_access_token"):
            return auth.create_access_token(c)
    except Exception:
        pass
    # fallback to jose/pyjwt with env secrets
    secret = os.getenv("SECRET_KEY", "dev-secret-change-me")
    alg    = os.getenv("ALGORITHM", "HS256")
    try:
        from jose import jwt as jj
        return jj.encode(c, secret, algorithm=alg)
    except Exception:
        import jwt as pj
        t = pj.encode(c, secret, algorithm=alg)
        return t.decode() if isinstance(t, bytes) else t

print(json.dumps({"access_token": make_token(claims)}))
