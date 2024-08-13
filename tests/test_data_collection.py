import unittest
from src.data_collection import fetch_wikipedia_page

class TestDataCollection(unittest.TestCase):

    def test_fetch_wikipedia_page(self):
        title = "Natural language processing"
        content = fetch_wikipedia_page(title)
        self.assertTrue(len(content) > 0)

    def test_fetch_invalid_page(self):
        title = "ThisPageDoesNotExist12345"
        with self.assertRaises(ValueError):
            fetch_wikipedia_page(title)

if __name__ == '__main__':
    unittest.main()
