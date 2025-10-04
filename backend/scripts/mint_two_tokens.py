from __future__ import annotations
import os, sys, json, datetime as dt
sys.path.insert(0, r"D:\whisper-laced")

def make_token(claims):
    # Prefer your project function
    try:
        from backend.core import auth
        if hasattr(auth, "create_access_token"):
            return auth.create_access_token(claims)
    except Exception:
        pass
    # Fallback to jose/pyjwt using app/env secrets
    secret = os.getenv("SECRET_KEY", "dev-secret-change-me")
    alg    = os.getenv("ALGORITHM", "HS256")
    try:
        from jose import jwt as jj
        return jj.encode(claims, secret, algorithm=alg)
    except Exception:
        import jwt as pj
        tok = pj.encode(claims, secret, algorithm=alg)
        return tok.decode() if isinstance(tok, bytes) else tok

uid = os.environ.get("UID")
email = os.environ.get("EMAIL")

base = {"role":"admin","roles":["admin"], "exp": dt.datetime.utcnow()+dt.timedelta(minutes=60)}
t1 = make_token(dict(sub=str(uid), email=email, **base))    # sub=id
t2 = make_token(dict(sub=email,     email=email, **base))    # sub=email
print(json.dumps({"sub_id": t1, "sub_email": t2}))
