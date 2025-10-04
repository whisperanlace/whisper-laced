from fastapi import Header, HTTPException, status, Depends
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.models import User

def api_key_auth(x_api_key: str = Header(...), db: Session = Depends(get_db)) -> User:
    user = db.query(User).filter(User.api_key == x_api_key, User.api_key_active == True).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or inactive API key")
    return user

