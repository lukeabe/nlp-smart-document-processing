import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_text(text: str) -> str:
    text = re.sub(r'\[\d+\]', '', text)  # Remove references
    text = re.sub(r'\W+', ' ', text)  # Remove special characters and numbers
    
    tokens = word_tokenize(text.lower())
    
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    
    processed_text = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    
    return ' '.join(processed_text)
