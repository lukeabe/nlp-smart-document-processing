import os
from data_collection import fetch_wikipedia_content
from preprocessing import preprocess_text
from summarization import summarize_text
from sentiment_analysis import analyze_sentiment

def chunk_text(text, chunk_size=1024):
    """Splits the text into chunks that fit within the model's token limit."""
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

def summarize_large_text(text, chunk_size=1024):
    chunks = chunk_text(text, chunk_size)
    summaries = [summarize_text(chunk) for chunk in chunks]
    combined_summary = " ".join(summaries)
    return combined_summary

def main():
    user_agent = "YourAppName/1.0 (lukeabraham1175@gmail.com)"
    page_title = "Lacrosse"  # Example page title

    try:
        # Fetch the content
        content = fetch_wikipedia_content(page_title, user_agent)
        print(f"Loaded Content Length: {len(content)} characters")
        
        # Take a larger portion for testing
        large_content = content[:10000]  # Adjust the size as needed
        print(f"Large Content Length: {len(large_content)} characters")
        
        # Preprocess the content
        preprocessed_content = preprocess_text(large_content)
        print(f"Preprocessed Content Length: {len(preprocessed_content)} characters")
        
        # Summarize the content in chunks
        summary = summarize_large_text(preprocessed_content)
        print(f"Summary:\n{summary}")
        
        # Save the summary
        summary_path = os.path.join('data', page_title + '_summary.txt')
        with open(summary_path, 'w') as file:
            file.write(summary)
        print(f"Summary has been saved to '{summary_path}'.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
