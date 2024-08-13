import unittest
from src.summarization import summarize_text

class TestSummarization(unittest.TestCase):
    def test_summarize_text(self):
        raw_text = ("Machine learning (ML) is a field of artificial intelligence (AI) "
                    "that focuses on building systems that learn from data. "
                    "Machine learning algorithms improve their performance over time without being explicitly programmed.")
        summary = summarize_text(raw_text)
        self.assertTrue(len(summary) > 0)

if __name__ == "__main__":
    unittest.main()
