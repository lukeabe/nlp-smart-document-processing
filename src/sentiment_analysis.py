from transformers import pipeline

# Initialize the sentiment analysis pipeline
# Specify the model name and revision explicitly
sentiment_analyzer = pipeline(
    "sentiment-analysis", 
    model="distilbert-base-uncased-finetuned-sst-2-english", 
    revision="af0f99b"  # You can specify a different revision if needed
)

def analyze_sentiment(text: str) -> dict:
    # Perform sentiment analysis
    sentiment = sentiment_analyzer(text)
    # Return the first result (assuming the output is a list)
    return sentiment[0]
