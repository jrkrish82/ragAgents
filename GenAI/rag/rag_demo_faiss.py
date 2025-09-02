import os
import json
import numpy as np
import faiss
import requests
from langchain_ollama import OllamaLLM

OLLAMA_URL = "http://localhost:11434/api"
MODEL_NAME = "llama2:7b"
DOC_PATH = "doc.txt"
FAISS_INDEX_PATH = "faiss.index"
CHUNKS_PATH = "chunks.json"

def get_embedding(text: str):
    response = requests.post(
        f"{OLLAMA_URL}/embeddings",
        json={"model": MODEL_NAME, "prompt": text}
    )
    print("Embedding raw response:", response.text)  # Debug print
    return np.array(response.json()["embedding"], dtype="float32")

def chunk_document(doc_path):
    with open(doc_path, "r", encoding="utf-8") as f:
        text = f.read()
    return [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]

def build_faiss_index(chunks):
    embeddings = [get_embedding(chunk) for chunk in chunks]
    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.stack(embeddings))
    faiss.write_index(index, FAISS_INDEX_PATH)
    with open(CHUNKS_PATH, "w", encoding="utf-8") as f:
        json.dump(chunks, f)
    print(f"Indexed {len(chunks)} chunks.")

def load_faiss_index():
    index = faiss.read_index(FAISS_INDEX_PATH)
    with open(CHUNKS_PATH, "r", encoding="utf-8") as f:
        chunks = json.load(f)
    return index, chunks

def retrieve(query, top_k=3):
    index, chunks = load_faiss_index()
    query_emb = get_embedding(query).reshape(1, -1)
    D, I = index.search(query_emb, top_k)
    return [chunks[i] for i in I[0]]

def generate_answer(query, context):
    llm = OllamaLLM(model=MODEL_NAME)
    prompt = [
        {
            "role": "system",
            "content": (
                "You are a helpful assistant. Use the provided context to answer the user's question."
            )
        },
        {
            "role": "user",
            "content": (
                "Context:\n" + "\n---\n".join(context) +
                f"\n\nQuestion: {query}\nAnswer:"
            )
        }
    ]
    print("Prompt sent to OllamaLLM:", prompt)
    response = llm.invoke(prompt)
    print("LLM response:", response)
    return response

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--build", action="store_true", help="Build FAISS index from doc.txt")
    parser.add_argument("--ask", type=str, help="Ask a question")
    args = parser.parse_args()

    if args.build:
        chunks = chunk_document(DOC_PATH)
        build_faiss_index(chunks)
    elif args.ask:
        context = retrieve(args.ask)
        answer = generate_answer(args.ask, context)
        print("Answer:", answer)
    else:
        print("Use --build to index doc.txt or --ask <question> to query.")
