from transformers import pipeline

summarizer = pipeline("summarization")

def summarize_text(text: str) -> str:
    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
    return summary[0]['summary_text']
