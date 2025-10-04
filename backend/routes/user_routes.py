import os
from fastapi import APIRouter, Depends
from sqlalchemy import MetaData, Table, select, insert, update
from sqlalchemy.orm import Session
from secrets import token_urlsafe

from backend.db import get_db, engine

DEV_NO_AUTH = os.getenv("DEV_NO_AUTH", "0") == "1"

if DEV_NO_AUTH:
    class _DevUser: id = 1
    def get_current_user():
        return _DevUser()
else:
    from backend.core import auth
    get_current_user = auth.get_current_user

router = APIRouter(prefix="/user", tags=["user"])

def _users_table():
    md = MetaData()
    return Table("users", md, autoload_with=engine)

@router.get("/apikey")
def get_api_key(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    users = _users_table()
    row = db.execute(
        select(users.c.id, users.c.api_key).where(users.c.id == current_user.id)
    ).fetchone()

    if row and row.api_key:
        return {"apikey": row.api_key}

    new_key = token_urlsafe(32)
    if row is None:
        try:
            db.execute(insert(users).values(id=current_user.id, api_key=new_key))
            db.commit()
            return {"apikey": new_key}
        except Exception:
            pass  # fall through to update trick

    db.execute(
        update(users).where(users.c.id == current_user.id).values(api_key=new_key)
    )
    db.commit()
    return {"apikey": new_key}

@router.post("/apikey/rotate")
def rotate_api_key(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    users = _users_table()
    new_key = token_urlsafe(32)
    existing = db.execute(
        select(users.c.id).where(users.c.id == current_user.id)
    ).fetchone()
    if existing is None:
        try:
            db.execute(insert(users).values(id=current_user.id, api_key=new_key))
        except Exception:
            pass
    db.execute(
        update(users).where(users.c.id == current_user.id).values(api_key=new_key)
    )
    db.commit()
    return {"apikey": new_key}
