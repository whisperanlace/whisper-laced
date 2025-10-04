from __future__ import annotations
import base64, hashlib, hmac, time, os
from urllib.parse import urlencode, quote

_SECRET = os.getenv("SECRET_KEY", "CHANGE_ME").encode("utf-8")

def sign(path: str, exp_seconds: int = 600) -> str:
    """Return a query string 'exp=..&sig=..' for path (no host), exp offset seconds."""
    exp = int(time.time()) + int(exp_seconds)
    msg = f"{path}?exp={exp}".encode("utf-8")
    sig = hmac.new(_SECRET, msg, hashlib.sha256).digest()
    return urlencode({"exp": exp, "sig": base64.urlsafe_b64encode(sig).decode().rstrip("=")})

def verify(path: str, exp: int, sig_b64: str) -> bool:
    if exp < int(time.time()):
        return False
    msg = f"{path}?exp={exp}".encode("utf-8")
    raw = base64.urlsafe_b64decode(sig_b64 + "===")
    expect = hmac.new(_SECRET, msg, hashlib.sha256).digest()
    return hmac.compare_digest(raw, expect)