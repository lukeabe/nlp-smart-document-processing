import unittest
from src.preprocessing import preprocess_text

class TestPreprocessing(unittest.TestCase):
    def test_preprocess_text(self):
        raw_text = "Machine learning [1] is a field of artificial intelligence."
        processed_text = preprocess_text(raw_text)
        self.assertIn("machine learning", processed_text)
        self.assertNotIn("[1]", processed_text)

if __name__ == "__main__":
    unittest.main()
