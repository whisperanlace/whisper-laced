import argparse
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from backend.db import SessionLocal, engine, Base
from backend.core import auth as core_auth
from backend.models import User

PASSWORD_FIELDS = ("password_hash", "hashed_password", "password")

def set_password(user, plaintext: str):
    material = core_auth.get_password_hash(plaintext)
    for field in PASSWORD_FIELDS:
        if hasattr(user, field):
            setattr(user, field, material)
            return field
    setattr(user, "password_hash", material)
    return "password_hash"

def ensure_tables():
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        print(f"[seed_user] WARN: create_all failed: {e}")

def upsert_user(email: str, password: str, is_admin: bool):
    ensure_tables()
    db: Session = SessionLocal()
    try:
        user = db.query(User).filter(User.email == email).first()
        created = False
        if not user:
            user = User(email=email)
            created = True

        field_used = set_password(user, password)

        for attr, val in [
            ("is_active", True),
            ("is_admin", is_admin),
            ("active", True),
            ("admin", is_admin),
            ("verified", True),
        ]:
            if hasattr(user, attr):
                setattr(user, attr, val)

        if created:
            db.add(user)
        db.commit()
        db.refresh(user)
        return created, field_used
    except IntegrityError:
        db.rollback()
        user = db.query(User).filter(User.email == email).first()
        return False, "unknown"
    finally:
        db.close()

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--email", required=True)
    p.add_argument("--password", required=True)
    p.add_argument("--admin", action="store_true")
    args = p.parse_args()
    created, field = upsert_user(args.email, args.password, args.admin)
    print(f"[seed_user] {'CREATED' if created else 'UPDATED'} {args.email} (password -> {field})")

if __name__ == "__main__":
    main()

