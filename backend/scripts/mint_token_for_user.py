from __future__ import annotations
import os, sys, json, datetime as dt
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path: sys.path.insert(0, ROOT)

def mint(user_id: str, email: str, role: str = "admin"):
    claims = {"sub": str(user_id), "email": email, "role": role, "roles": [role]}
    # Prefer your app's token creator
    try:
        from backend.core import auth
        if hasattr(auth, "create_access_token"):
            tok = auth.create_access_token(claims)
            print(json.dumps({"token": tok}))
            return
    except Exception:
        pass
    # Fallback: jose or pyjwt using env vars
    secret = os.getenv("SECRET_KEY", "dev-secret-change-me")
    alg    = os.getenv("ALGORITHM", "HS256")
    mins   = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))
    payload = claims.copy()
    payload["exp"] = dt.datetime.utcnow() + dt.timedelta(minutes=mins)
    try:
        from jose import jwt as jose_jwt
        tok = jose_jwt.encode(payload, secret, algorithm=alg)
        print(json.dumps({"token": tok}))
        return
    except Exception:
        pass
    import jwt as pyjwt
    tok = pyjwt.encode(payload, secret, algorithm=alg)
    # PyJWT on some versions returns bytes; normalize to str
    if isinstance(tok, bytes):
        tok = tok.decode("utf-8")
    print(json.dumps({"token": tok}))

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--user_id", required=True)
    ap.add_argument("--email", required=True)
    ap.add_argument("--role", default="admin")
    a = ap.parse_args()
    mint(a.user_id, a.email, a.role)
