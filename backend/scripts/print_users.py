from backend.db import SessionLocal, engine, Base
from backend.models import User
from sqlalchemy import inspect

def main():
    db = SessionLocal()
    try:
        insp = inspect(engine)
        print("[print_users] tables:", insp.get_table_names())
        cols = [c.name for c in User.__table__.columns]
        print("[print_users] User columns:", cols)

        users = db.query(User).all()
        print(f"[print_users] count: {len(users)}")
        for u in users:
            # print common identity fields if present
            bits = []
            for k in ("id", "email", "email_address", "username"):
                if hasattr(u, k):
                    bits.append(f"{k}={getattr(u,k)}")
            print("  -", ", ".join(bits) if bits else repr(u))
    finally:
        db.close()

if __name__ == "__main__":
    main()

