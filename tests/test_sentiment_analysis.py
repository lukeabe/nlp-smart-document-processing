import unittest
from src.sentiment_analysis import analyze_sentiment

class TestSentimentAnalysis(unittest.TestCase):

    def test_analyze_sentiment(self):
        positive_text = "I absolutely love this product! It's amazing and works perfectly."
        sentiment = analyze_sentiment(positive_text)
        self.assertEqual(sentiment['label'], 'POSITIVE')

if __name__ == '__main__':
    unittest.main()
