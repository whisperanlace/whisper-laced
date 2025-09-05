# utils/db_utils.py
from typing import Generator, Optional, Callable, Any
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, Session
import os
import logging

logger = logging.getLogger(__name__)

# Expect DATABASE_URL in config/settings or environment
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://user:pass@localhost:5432/laced")

# Use pool_pre_ping to avoid stale connections in production
engine = create_engine(DATABASE_URL, pool_pre_ping=True, pool_size=20, max_overflow=40)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db_session() -> Generator[Session, None, None]:
    """
    Dependency / context manager for DB sessions. Yields SQLAlchemy session and ensures cleanup.
    Use: with get_db_session() as session: ...
    Or integrate with FastAPI dependency injection.
    """
    session: Optional[Session] = None
    try:
        session = SessionLocal()
        yield session
    except Exception:
        if session:
            session.rollback()
        logger.exception("Database session error")
        raise
    finally:
        if session:
            session.close()

def run_in_transaction(fn: Callable[..., Any], *args, **kwargs) -> Any:
    """
    Helper to execute a function with transactional guarantees.
    The function receives a session keyword arg if it accepts it.
    """
    session = SessionLocal()
    try:
        result = fn(session=session, *args, **kwargs)
        session.commit()
        return result
    except Exception:
        session.rollback()
        logger.exception("Transaction failed, rolled back")
        raise
    finally:
        session.close()
