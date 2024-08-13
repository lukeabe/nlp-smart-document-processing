import unittest
from src.sentiment_analysis import analyze_sentiment

class TestSentimentAnalysis(unittest.TestCase):
    def test_analyze_sentiment(self):
        text = "Machine learning is transforming the world."
        sentiment = analyze_sentiment(text)
        self.assertIn('label', sentiment)
        self.assertIn('score', sentiment)

if __name__ == "__main__":
    unittest.main()
