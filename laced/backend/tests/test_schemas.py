# -*- coding: utf-8 -*-
from schemas.user_schema import UserCreate, UserRead

def test_user_schema_validation():
    data = {"email": "schema@example.com", "password": "pass123"}
    user = UserCreate(**data)
    assert user.email == "schema@example.com"

    read_data = {"id": 1, "email": "schema@example.com"}
    user_read = UserRead(**read_data)
    assert user_read.id == 1
