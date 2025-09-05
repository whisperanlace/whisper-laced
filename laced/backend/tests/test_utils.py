# -*- coding: utf-8 -*-
import pytest
from utils.crypto_utils import hash_password, verify_password

def test_password_hashing():
    password = "secure123"
    hashed = hash_password(password)
    assert verify_password(password, hashed) is True
    assert verify_password("wrongpass", hashed) is False
