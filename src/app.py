from flask import Flask, request, jsonify
from data_collection import fetch_wikipedia_page
from preprocessing import preprocess_text
from summarization import summarize_text
from sentiment_analysis import analyze_sentiment

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    title = data.get('title')
    
    if not title:
        return jsonify({'error': 'Title is required'}), 400
    
    try:
        page_content = fetch_wikipedia_page(title)
        processed_content = preprocess_text(page_content)
        summary = summarize_text(processed_content)
        sentiment = analyze_sentiment(summary)
        
        return jsonify({
            'title': title,
            'summary': summary,
            'sentiment': sentiment
        })
    except ValueError as e:
        return jsonify({'error': str(e)}), 404

if __name__ == '__main__':
    app.run(debug=True)
