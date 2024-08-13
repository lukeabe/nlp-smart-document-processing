import os
from data_collection import fetch_wikipedia_content
from preprocessing import preprocess_text
from summarization import summarize_text
from sentiment_analysis import analyze_sentiment

def main():
    user_agent = "YourAppName/1.0 (lukeabraham1175@gmail.com)"
    page_title = "Lacrosse"  # Example page title

    try:
        # Fetch the content
        content = fetch_wikipedia_content(page_title, user_agent)
        print(f"Loaded Content Length: {len(content)} characters")
        
        # Take a small portion for testing
        small_content = content[:100]  # Adjust the size as needed for testing
        print(f"Small Content Length: {len(small_content)} characters")
        
        # Preprocess the content
        preprocessed_content = preprocess_text(small_content)
        print(f"Preprocessed Content Length: {len(preprocessed_content)} characters")
        
        # Summarize the content
        summary = summarize_text(preprocessed_content)
        print(f"Summary:\n{summary}")
        
        # Analyze the sentiment of the summary
        sentiment = analyze_sentiment(summary)
        print(f"Sentiment Analysis:\n{sentiment}")
        
        # Save the summary and sentiment analysis
        summary_path = os.path.join('data', f'{page_title}_summary.txt')
        sentiment_path = os.path.join('data', f'{page_title}_sentiment.txt')
        
        # Ensure the 'data' directory exists
        os.makedirs('data', exist_ok=True)
        
        # Save the summary
        with open(summary_path, 'w') as file:
            file.write(summary)
        print(f"Summary has been saved to '{summary_path}'.")
        
        # Save the sentiment analysis
        with open(sentiment_path, 'w') as file:
            file.write(f"Sentiment Analysis: {sentiment}\n")
        print(f"Sentiment analysis has been saved to '{sentiment_path}'.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
