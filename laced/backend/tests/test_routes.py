# -*- coding: utf-8 -*-
import pytest

@pytest.mark.asyncio
async def test_home_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to Laced API"
