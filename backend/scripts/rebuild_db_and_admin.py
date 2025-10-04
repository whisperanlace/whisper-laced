import sys
sys.path.insert(0, r"D:/whisper-laced")
from backend.db import engine, Base, SessionLocal
from backend.models import User
from backend.core.password import get_password_hash

# Create tables
Base.metadata.create_all(bind=engine)
print("✅ schema at", engine.url)

# Upsert admin
db = SessionLocal()
try:
    email = "whisperandlaced@gmail.com"
    pwd   = "AandD03022022$"
    u = db.query(User).filter(User.email==email).first()
    if not u:
        u = User(email=email, username="whisperandlaced")
        db.add(u); db.flush()
    u.hashed_password = get_password_hash(pwd)
    db.commit()
    print({"ok": True, "id": u.id, "email": u.email})
finally:
    db.close()

