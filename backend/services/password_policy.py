import re
from backend.config.settings import settings

def validate_password(p: str) -> None:
    if len(p) < settings.PASSWORD_MIN_LENGTH:
        raise ValueError(f"Password must be at least {settings.PASSWORD_MIN_LENGTH} characters")
    if settings.PASSWORD_REQUIRE_UPPER and not re.search(r"[A-Z]", p): raise ValueError("Password needs an uppercase letter")
    if settings.PASSWORD_REQUIRE_LOWER and not re.search(r"[a-z]", p): raise ValueError("Password needs a lowercase letter")
    if settings.PASSWORD_REQUIRE_DIGIT and not re.search(r"\d", p):    raise ValueError("Password needs a digit")
    if settings.PASSWORD_REQUIRE_SYMBOL and not re.search(r"[^A-Za-z0-9\s]", p): raise ValueError("Password needs a symbol")
