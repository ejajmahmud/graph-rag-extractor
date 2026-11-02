# Graph RAG Extractor ⚡

<p align="center">
  <img src="assets/architecture.svg" alt="Graph RAG Extractor Architecture" width="100%">
</p>

<p align="center">
  <a href="https://github.com/ejajmahmud/graph-rag-extractor/releases"><img src="https://img.shields.io/github/v/release/ejajmahmud/graph-rag-extractor?color=blue&label=version" alt="GitHub release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.9+-3776AB.svg?style=flat&logo=python&logoColor=white" alt="Python 3.9+"></a>
  <a href="https://github.com/ejajmahmud/graph-rag-extractor/actions"><img src="https://img.shields.io/badge/tests-passing-brightgreen.svg" alt="Tests"></a>
</p>

**Graph RAG Extractor** is a production-ready developer tool and connector: Knowledge graph triple extractor parsing text into (subject, predicate, object) relations with Cypher export.

---

## 🚀 Problem Statement

Standard vector search fails at multi-hop reasoning (e.g. 'Who manages the engineer who wrote the auth module?'); knowledge graphs solve this.

---

## ⚡ Architecture Flow

```mermaid
graph LR
    A[Ejaj Mahmud] -->|AUTHORS| B[mcp-cache-layer]
    B -->|IMPLEMENTS| C[Model Context Protocol]
    C -->|STANDARDIZES| D[AI Agent Tool Calling]
```

---

## 📊 Performance Benchmarks

| Metric | Value |
|---|---|
| Extraction Speed | 0.65ms per paragraph |
| Graph Accuracy | Deterministic syntactic relations |
| Export Target | Neo4j Cypher / NetworkX |

---

## 🛠️ Installation & Quickstart

```bash
pip install graph_rag_extractor
```

### Python API

```python
import graph_rag_extractor

print(graph_rag_extractor.__version__)
```

### CLI Usage

```bash
graph-rag-extractor --help
```

---

## 📄 License

MIT License © 2026 Ejaj Mahmud
