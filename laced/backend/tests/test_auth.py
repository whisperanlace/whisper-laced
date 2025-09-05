# -*- coding: utf-8 -*-
import pytest
from fastapi.testclient import TestClient

@pytest.mark.asyncio
async def test_register_login(client: TestClient):
    # Register user
    response = client.post("/auth/register", json={
        "email": "test@example.com",
        "password": "password123"
    })
    assert response.status_code == 201

    # Login
    response = client.post("/auth/login", json={
        "email": "test@example.com",
        "password": "password123"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
