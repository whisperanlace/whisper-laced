from __future__ import annotations
import os, sys, json
sys.path.insert(0, r"D:\whisper-laced")
from sqlalchemy import text
from backend.db import engine, SessionLocal
info = {"engine_url": str(engine.url)}
if engine.url.get_backend_name() == "sqlite":
    info["sqlite_path"] = engine.url.database
db = SessionLocal()
try:
    users = db.execute(text("SELECT id, email FROM users ORDER BY id")).fetchall()
    info["users"] = [{"id": r[0], "email": r[1]} for r in users]
finally:
    db.close()
print(json.dumps(info))
