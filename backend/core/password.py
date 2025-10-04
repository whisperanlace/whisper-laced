from passlib.context import CryptContext

# Use a stable, no-72B-limit scheme to unblock you
ctx = CryptContext(
    schemes=["pbkdf2_sha256"],
    deprecated="auto",
)

def get_password_hash(password: str) -> str:
    return ctx.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return ctx.verify(plain_password, hashed_password)
