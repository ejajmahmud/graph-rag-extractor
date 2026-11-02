"""Knowledge graph triple extractor."""
import re
from typing import List, Tuple

class GraphExtractor:
    @staticmethod
    def extract_triples(text: str) -> List[Tuple[str, str, str]]:
        """Heuristic rule-based (subject, predicate, object) extractor."""
        triples = []
        sentences = re.split(r"[.!?]\s+", text)
        rel_pattern = re.compile(r"\b(is|has|uses|creates|builds|deploys|author of)\b", re.IGNORECASE)

        for s in sentences:
            m = rel_pattern.search(s)
            if m:
                subj = s[:m.start()].strip()
                pred = m.group(0).strip().upper().replace(" ", "_")
                obj = s[m.end():].strip().rstrip(".")
                if subj and obj:
                    triples.append((subj, pred, obj))
        return triples

    @staticmethod
    def to_cypher(triples: List[Tuple[str, str, str]]) -> List[str]:
        cypher = []
        for s, p, o in triples:
            cypher.append(f"MERGE (a:Entity {{name: '{s}'}}) MERGE (b:Entity {{name: '{o}'}}) MERGE (a)-[:{p}]->(b);")
        return cypher
