# tests/test_phase8_apikey.py
from types import SimpleNamespace

from fastapi.testclient import TestClient
from sqlalchemy import MetaData, Table, insert
from sqlalchemy.exc import IntegrityError

from backend.app.main import app
from backend.db import engine, SessionLocal

# Override auth dependency to return a stable user id=1 for tests only
try:
    from backend.core import auth
except Exception as e:
    raise RuntimeError(f"Auth module import failed: {e}")

app.dependency_overrides[auth.get_current_user] = lambda: SimpleNamespace(id=1)

def ensure_user_row():
    md = MetaData()
    users = Table("users", md, autoload_with=engine)
    with SessionLocal() as db:
        # Insert row id=1 if missing; ignore if other columns are NOT NULL
        try:
            db.execute(insert(users).values(id=1))
            db.commit()
        except IntegrityError:
            db.rollback()  # row exists or NOT NULL constraint tripped — that's fine

def test_get_apikey_creates_or_returns_key():
    ensure_user_row()
    client = TestClient(app)
    r = client.get("/user/apikey")
    assert r.status_code == 200, r.text
    data = r.json()
    assert "apikey" in data and isinstance(data["apikey"], str) and len(data["apikey"]) >= 20

def test_rotate_apikey_changes_key():
    ensure_user_row()
    client = TestClient(app)
    r1 = client.get("/user/apikey")
    assert r1.status_code == 200
    old_key = r1.json()["apikey"]

    r2 = client.post("/user/apikey/rotate")
    assert r2.status_code == 200
    new_key = r2.json()["apikey"]

    assert new_key and new_key != old_key
