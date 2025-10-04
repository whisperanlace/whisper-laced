import time, uuid, os
import jwt, secrets
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext

SECRET = os.getenv("SECRET_KEY", "CHANGE_ME_64_CHAR_MIN")
ALGO = "HS256"

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(plain: str) -> str:
    return pwd_ctx.hash(plain)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_ctx.verify(plain, hashed)

def create_access_token(sub: str, minutes: int = 60) -> str:
    now = int(time.time())
    payload = {"sub": sub, "iat": now, "exp": now + minutes*60}
    return jwt.encode(payload, SECRET, algorithm=ALGO)

def decode_token(token: str) -> dict:
    return jwt.decode(token, SECRET, algorithms=[ALGO])

def new_random_token() -> str:
    return secrets.token_hex(32)

def expires_in_minutes(m: int):
    return datetime.now(timezone.utc) + timedelta(minutes=m)
