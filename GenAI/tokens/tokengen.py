from transformers import GPT2Tokenizer
import ssl

try:
    # Load the pre-trained GPT-2 tokenizer from a local directory
    tokenizer = GPT2Tokenizer.from_pretrained(
        "/c:/Krishna/cashflowAgent/repo/113720/GenAI/tokens/gpt2_local",
        local_files_only=True
    )
except Exception as e:
    print("Failed to load GPT-2 tokenizer locally. Please download the files from https://huggingface.co/gpt2 and place them in the specified directory.")
    print("Error:", e)
    exit(1)

# Your input text
text = "I love Python and transformers!"

# Tokenize the input
tokens = tokenizer.tokenize(text)
token_ids = tokenizer.convert_tokens_to_ids(tokens)

# Print results
print("Original Text:", text)
print("Tokens:", tokens)
print("Token IDs:", token_ids)

# Optional: Encode directly (tokens + ids)
encoded = tokenizer(text)
print("Encoded Output:", encoded)

# Decode back from IDs to string
decoded_text = tokenizer.decode(token_ids)
print("Decoded Text:", decoded_text)