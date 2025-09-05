# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Load DB connection string from env, fallback to SQLite dev
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./dev.db")

# If SQLite file, adjust connect args
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

# Engine = main connection to DB
engine = create_engine(
    DATABASE_URL,
    echo=False,       # set True for SQL debug logging
    future=True,
    connect_args=connect_args
)

# SessionLocal = session factory for each request
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    future=True
)

# Base = class models inherit from
Base = declarative_base()

# Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
