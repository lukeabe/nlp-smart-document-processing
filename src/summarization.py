from transformers import pipeline

def split_text(text: str, max_length: int) -> list:
    """Split text into chunks of max_length tokens."""
    tokens = text.split()  # Simple whitespace tokenization
    chunks = [tokens[i:i + max_length] for i in range(0, len(tokens), max_length)]
    return [' '.join(chunk) for chunk in chunks]

def summarize_text(text: str) -> str:
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    
    # Split the text into chunks if it's too long
    max_chunk_length = 1024  # Adjust this if necessary
    chunks = split_text(text, max_chunk_length)
    
    summaries = []
    for chunk in chunks:
        summary = summarizer(chunk, max_length=150, min_length=50, do_sample=False)
        summaries.append(summary[0]['summary_text'])
    
    return ' '.join(summaries)
