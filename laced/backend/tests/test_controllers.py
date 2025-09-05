# -*- coding: utf-8 -*-
import pytest
from controllers.user_controller import UserController

@pytest.mark.asyncio
async def test_controller_create_user(db_session):
    controller = UserController(db_session)
    user = await controller.create_user(email="ctrl@example.com", password="pass123")
    assert user.email == "ctrl@example.com"
