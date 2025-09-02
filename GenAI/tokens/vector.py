import re

def chunk_text(text, chunk_size=2):
    # Split text into sentences as chunks
    sentences = re.split(r'(?<=[.!?]) +', text)
    # Group sentences into chunks of chunk_size
    chunks = [' '.join(sentences[i:i+chunk_size]) for i in range(0, len(sentences), chunk_size)]
    return chunks

def simple_vectorizer(chunk):
    # Dummy vectorizer: count word occurrences
    words = chunk.lower().split()
    vector = {}
    for word in words:
        vector[word] = vector.get(word, 0) + 1
    return vector

if __name__ == "__main__":
    text = input("Enter your text: ")
    chunks = chunk_text(text, chunk_size=2)
    print("\nChunks and their vectors:")
    for i, chunk in enumerate(chunks):
        vector = simple_vectorizer(chunk)
        # print(f"Chunk {i+1}: {chunk}")
        print(f"Vector values for chunk {i+1}: {list(vector.values())}\n")
