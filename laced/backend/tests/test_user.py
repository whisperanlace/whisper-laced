# -*- coding: utf-8 -*-
import pytest

@pytest.mark.asyncio
async def test_user_crud(client):
    # Create user
    response = client.post("/users/", json={"email": "user@example.com", "password": "pass123"})
    assert response.status_code == 201
    user_id = response.json()["id"]

    # Get user
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["email"] == "user@example.com"

    # Update user
    response = client.put(f"/users/{user_id}", json={"email": "user2@example.com"})
    assert response.status_code == 200
    assert response.json()["email"] == "user2@example.com"

    # Delete user
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 204
