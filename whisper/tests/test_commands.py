# tests/test_commands.py
import unittest
from cogs.prompts import PromptCog
from core.bot import bot

class TestPromptCommands(unittest.IsolatedAsyncioTestCase):
    async def test_dummy(self):
        self.assertTrue(True)
