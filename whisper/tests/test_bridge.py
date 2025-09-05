# tests/test_bridge.py
import unittest
from core.bridge import laced_bridge

class TestBridge(unittest.IsolatedAsyncioTestCase):
    async def test_send_prompt_error(self):
        result = await laced_bridge.send_prompt("Test", "dummy_user")
        # Should return either images or error dict
        self.assertIsInstance(result, dict)
