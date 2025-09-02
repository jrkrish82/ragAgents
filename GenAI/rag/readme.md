# Simple RAG Demo with Ollama & Llama2:7b

## Prerequisites
- Ollama running locally with Llama2:7b model pulled.
- Python 3.x
- `requests` and `numpy` libraries.
- (Optional) If you need a third-party `cmd` package, install with:
  ```
  pip install cmd2
  ```
  > Note: The built-in `cmd` module does not require installation.

## Usage

### 1. Build the FAISS index from your document

Make sure your document is named `doc.txt` and placed in the same folder as the script.

```
python rag_demo_faiss.py --build
```

### 2. Ask a question

```
python rag_demo_faiss.py --ask "Your question here"
```

The script will retrieve relevant context from the indexed document and generate an answer using Llama2:7b via Ollama.

## Notes
- The vector DB is stored as `vector_db.json` in the project folder.
- Document chunking is simple (by paragraphs). For better results, use more advanced chunking.
