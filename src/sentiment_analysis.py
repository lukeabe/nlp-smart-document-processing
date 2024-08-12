from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self):
        self.analyzer = pipeline('sentiment-analysis')

    def analyze_sentiment(self, text):
        result = self.analyzer(text)
        return result[0]
