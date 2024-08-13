import unittest
from src.preprocessing import preprocess_text

class TestPreprocessing(unittest.TestCase):

    def test_preprocess_text(self):
        raw_text = "This is a test sentence. It has some [1] references and special #characters!"
        processed_text = preprocess_text(raw_text)
        expected_text = "test sentence reference special character"
        self.assertIn(expected_text, processed_text)

if __name__ == '__main__':
    unittest.main()
