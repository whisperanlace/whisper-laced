# utils/crypto_utils.py
from typing import Tuple
import secrets
import hashlib
import hmac
import base64
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """
    Securely hash a plaintext password using bcrypt (via passlib).
    """
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    """
    Verify a plaintext password against a bcrypt hash.
    """
    return pwd_context.verify(password, hashed)

def random_token_urlsafe(length: int = 32) -> str:
    """Generate cryptographically secure random URL-safe token."""
    return secrets.token_urlsafe(length)

def hmac_sha256(message: bytes, key: bytes) -> str:
    """
    Compute HMAC-SHA256 and return base64-encoded digest.
    Useful for signing webhooks or external callbacks.
    """
    mac = hmac.new(key, message, hashlib.sha256).digest()
    return base64.b64encode(mac).decode("utf-8")
