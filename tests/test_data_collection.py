import unittest
from src.data_collection import fetch_wikipedia_page

class TestDataCollection(unittest.TestCase):
    def test_fetch_wikipedia_page(self):
        result = fetch_wikipedia_page("Machine learning")
        self.assertIsNotNone(result)
        self.assertTrue(len(result) > 0)

if __name__ == "__main__":
    unittest.main()
