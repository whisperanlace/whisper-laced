from backend.db import Base, engine, SessionLocal
from backend.models import *  # imports all models via backend/models/__init__.py
from passlib.hash import bcrypt

def ensure_tiers(db):
    from backend.models import Tier
    names = {"Standard", "Premium"}
    existing = {t.name for t in db.query(Tier).all()}
    for name in names - existing:
        db.add(Tier(name=name))
    db.commit()

def ensure_default_user(db):
    from backend.models import User
    u = db.query(User).filter(User.email == "test@example.com").first()
    if not u:
        u = User(
            username="testuser",
            email="test@example.com",
            hashed_password=bcrypt.hash("password123"),
        )
        db.add(u)
        db.commit()

if __name__ == "__main__":
    # create all tables
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        ensure_tiers(db)
        ensure_default_user(db)
        print("? DB bootstrap complete.")
    finally:
        db.close()

