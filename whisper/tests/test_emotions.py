# tests/test_emotions.py
import unittest
from personality.emotions import apply_emotion

class TestEmotions(unittest.TestCase):
    def test_apply_happy(self):
        text = "Hello"
        result = apply_emotion(text, "happy")
        self.assertIn("😊", result)
