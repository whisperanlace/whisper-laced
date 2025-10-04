#!/usr/bin/env python
import sys
sys.path.insert(0, r"D:\whisper-laced")

from backend.db import SessionLocal, engine, Base
from backend.models import User
from backend.core.password import get_password_hash

def main(email: str, password: str):
    # ensure tables exist
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        u = db.query(User).filter(User.email == email).first()
        if not u:
            u = User(email=email, username=email.split("@")[0])
            db.add(u)
        # use pbkdf2_sha256 from backend.core.password
        u.hashed_password = get_password_hash(password)
        db.commit()
        db.refresh(u)
        print({"id": u.id, "email": u.email})
    finally:
        db.close()

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--email", required=True)
    ap.add_argument("--password", required=True)
    args = ap.parse_args()
    main(args.email, args.password)

