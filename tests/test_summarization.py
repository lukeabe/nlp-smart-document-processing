import unittest
from src.summarization import summarize_text

class TestSummarization(unittest.TestCase):

    def test_summarize_text(self):
        long_text = "Natural language processing (NLP) is a field of artificial intelligence " \
                    "that focuses on the interaction between computers and humans through natural language. " \
                    "The ultimate goal of NLP is to enable computers to understand, interpret, and generate " \
                    "human language in a way that is both valuable and meaningful. NLP techniques rely heavily " \
                    "on machine learning and deep learning algorithms to process and analyze large volumes of text data."
        
        summary = summarize_text(long_text)
        self.assertTrue(len(summary) < len(long_text))

if __name__ == '__main__':
    unittest.main()
