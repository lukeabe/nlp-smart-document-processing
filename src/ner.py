import spacy

class NERExtractor:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def extract_entities(self, text):
        doc = self.nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        return entities
