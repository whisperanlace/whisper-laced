# utils/token_utils.py
from typing import Dict, Any, Optional
import time
import jwt  # PyJWT
import logging

logger = logging.getLogger(__name__)

# These constants should be provided via config/settings.py in production.
JWT_ALGORITHM = "HS256"

def create_jwt(payload: Dict[str, Any], secret: str, expires_in: int = 3600) -> str:
    """
    Create a JWT with 'exp' claim set to now + expires_in seconds.
    """
    now = int(time.time())
    data = payload.copy()
    data["iat"] = now
    data["exp"] = now + expires_in
    token = jwt.encode(data, secret, algorithm=JWT_ALGORITHM)
    if isinstance(token, bytes):
        token = token.decode("utf-8")
    return token

def decode_jwt(token: str, secret: str, verify_exp: bool = True) -> Dict[str, Any]:
    """
    Decode JWT and return payload. Raises jwt exceptions on failure.
    """
    options = {"verify_exp": verify_exp}
    payload = jwt.decode(token, secret, algorithms=[JWT_ALGORITHM], options=options)
    return payload
