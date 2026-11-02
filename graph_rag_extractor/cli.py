"""Command line interface for graph-rag-extractor."""
from .extractor import GraphExtractor

def main():
    text = "Antigravity creates autonomous agents. Python is the language."
    triples = GraphExtractor.extract_triples(text)
    print("Extracted Triples:", triples)
    print("Cypher DDL:", GraphExtractor.to_cypher(triples))

if __name__ == "__main__":
    main()
