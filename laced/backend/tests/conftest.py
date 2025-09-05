# -*- coding: utf-8 -*-
"""
Pytest fixtures for testing Laced.
Includes test database, client, and reusable objects.
"""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from config.database import Base, get_db_session
from config.settings import settings

# Setup test database
TEST_DATABASE_URL = settings.DATABASE_URL + "_test"
engine = create_engine(TEST_DATABASE_URL, future=True)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Override dependency
def override_get_db_session():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db_session] = override_get_db_session

# Pytest fixtures
@pytest.fixture(scope="session")
def client():
    # Create tables for testing
    Base.metadata.create_all(bind=engine)
    yield TestClient(app)
    # Drop tables after tests
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def db_session():
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
