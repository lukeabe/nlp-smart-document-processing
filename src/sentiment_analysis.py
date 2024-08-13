from transformers import pipeline

# Initialize the sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_sentiment(text: str) -> dict:
    # Perform sentiment analysis
    sentiment = sentiment_analyzer(text)
    # Return the first result (assuming the output is a list)
    return sentiment[0]
