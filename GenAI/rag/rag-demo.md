# Step-by-step Explanation of `rag_demo_faiss.py`

## 1. Imports and Constants
- Imports necessary libraries: `os`, `json`, `numpy`, `faiss`, `requests`, and `OllamaLLM` from `langchain_ollama`.
- Sets constants for Ollama API URL, model name, document path, FAISS index path, and chunks path.

## 2. Embedding Generation
- `get_embedding(text: str)`: Sends a POST request to the Ollama API to get an embedding vector for the given text using the specified model.

## 3. Document Chunking
- `chunk_document(doc_path)`: Reads the document and splits it into chunks separated by double newlines. Returns a list of non-empty chunks.

## 4. Building the FAISS Index
- `build_faiss_index(chunks)`: 
  - Gets embeddings for each chunk.
  - Creates a FAISS index (`IndexFlatL2`) and adds the embeddings.
  - Saves the index and the chunks to disk.

## 5. Loading the FAISS Index
- `load_faiss_index()`: Loads the FAISS index and the chunks from disk for retrieval.

## 6. Retrieval
- `retrieve(query, top_k=3)`: 
  - Loads the index and chunks.
  - Gets the embedding for the query.
  - Searches the index for the top-k most similar chunks.
  - Returns the retrieved chunks.

## 7. Answer Generation
- `generate_answer(query, context)`: 
  - Uses `OllamaLLM` to generate an answer based on the retrieved context and the user's question.
  - Constructs a prompt with system and user roles.
  - Invokes the LLM and returns the response.

## 8. Command-line Interface
- Uses `argparse` to provide two options:
  - `--build`: Builds the FAISS index from `doc.txt`.
  - `--ask <question>`: Retrieves relevant context and generates an answer for the question.

## Usage
- Run with `--build` to index the document.
- Run with `--ask "<your question>"` to get an answer based on the indexed document.
