# tests/test_personality.py
import unittest
from personality import base_persona

class TestPersonality(unittest.TestCase):
    def test_base_greeting(self):
        response = base_persona.respond("greeting")
        self.assertIn("Hello", response)
