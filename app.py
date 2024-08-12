from flask import Flask, request, jsonify
import torch
from torch.utils.data import DataLoader
from src.classification import DocumentClassifier, preprocess_data, build_vocab
from src.ner import NERExtractor
from src.summarization import TextSummarizer
from src.sentiment_analysis import SentimentAnalyzer
from src.preprocessing import preprocess_text
from src.utils import load_document
from torchtext.data.utils import get_tokenizer

app = Flask(__name__)

# Initialize components
embedding_dim = 128
hidden_dim = 64
output_dim = 1

# Prepare the tokenizer and vocabulary
tokenizer = get_tokenizer('basic_english')
documents = ["This is a sample document for vocabulary creation."]  # Placeholder for building vocab
vocab = build_vocab(documents, tokenizer)

classifier = DocumentClassifier(vocab_size=len(vocab), embedding_dim=embedding_dim, hidden_dim=hidden_dim, output_dim=output_dim)
ner_extractor = NERExtractor()
summarizer = TextSummarizer()
sentiment_analyzer = SentimentAnalyzer()

@app.route('/process_document', methods=['POST'])
def process_document():
    document = request.files['document']
    text = document.read().decode('utf-8')
    
    processed_text = preprocess_text(text)
    
    dataset = preprocess_data([processed_text], [0], vocab=vocab, tokenizer=tokenizer)
    data_loader = DataLoader(dataset, batch_size=1)
    
    for text_tensor, _ in data_loader:
        doc_classification = classifier.predict(text_tensor).tolist()
    
    doc_entities = ner_extractor.extract_entities(processed_text)
    doc_summary = summarizer.summarize(processed_text)
    doc_sentiment = sentiment_analyzer.analyze_sentiment(processed_text)
    
    results = {
        "classification": doc_classification,
        "entities": doc_entities,
        "summary": doc_summary,
        "sentiment": doc_sentiment
    }
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
