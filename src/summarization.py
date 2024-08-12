from transformers import pipeline

class TextSummarizer:
    def __init__(self):
        self.summarizer = pipeline('summarization')

    def summarize(self, text):
        summary = self.summarizer(text, max_length=50, min_length=25, do_sample=False)
        return summary[0]['summary_text']
