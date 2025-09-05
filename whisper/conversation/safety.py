# conversation/safety.py
import re

# Basic safety filters
BANNED_WORDS = ["nsfw", "illegal", "hack", "attack"]

def is_safe(message: str) -> bool:
    """Check if the message is safe for processing."""
    pattern = re.compile("|".join(BANNED_WORDS), re.IGNORECASE)
    if pattern.search(message):
        return False
    return True

def sanitize(message: str) -> str:
    """Redacts banned words."""
    sanitized = message
    for word in BANNED_WORDS:
        sanitized = re.sub(word, "[REDACTED]", sanitized, flags=re.IGNORECASE)
    return sanitized
