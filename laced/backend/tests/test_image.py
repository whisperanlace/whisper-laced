# -*- coding: utf-8 -*-
import pytest
from io import BytesIO

@pytest.mark.asyncio
async def test_image_upload(client):
    file_data = BytesIO(b"fake_image_data")
    response = client.post("/images/upload", files={"file": ("test.png", file_data, "image/png")})
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert "url" in data
