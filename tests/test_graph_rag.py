"""Unit tests for GraphExtractor."""
import unittest
from graph_rag_extractor.extractor import GraphExtractor

class TestGraphExtractor(unittest.TestCase):
    def test_triple_extraction(self):
        text = "Alice builds web applications."
        t = GraphExtractor.extract_triples(text)
        self.assertEqual(len(t), 1)
        self.assertEqual(t[0], ("Alice", "BUILDS", "web applications"))

if __name__ == "__main__":
    unittest.main()
