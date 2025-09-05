# -*- coding: utf-8 -*-
import pytest

@pytest.mark.asyncio
async def test_lora_training(client):
    response = client.post("/lora/train", json={"model_name": "test_lora"})
    assert response.status_code == 202
    data = response.json()
    assert data["status"] == "queued"
