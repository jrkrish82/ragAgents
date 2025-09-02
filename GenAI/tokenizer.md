# What is a Tokenizer?

A **tokenizer** is a tool used in Natural Language Processing (NLP) to split text into smaller pieces called tokens. These tokens are then converted into numerical IDs that machine learning models can process.

## Why Tokenize?

Language models like GPT-2 cannot process raw text directly. They need text to be broken down into tokens (words, subwords, or characters) and then mapped to numbers.

## Example

Suppose you have the text:

```
I love Python and transformers!
```

Using the GPT-2 tokenizer, this text is split into tokens:

```
['I', 'Ġlove', 'ĠPython', 'Ġand', 'Ġtransformers', '!']
```

Each token is then mapped to a unique ID:

```
[40, 837, 12190, 290, 22150, 0]
```

You can also decode these IDs back to the original text.

## How Tokenizers Work

- **Tokenization:** Splits text into tokens.
- **Encoding:** Converts tokens to IDs.
- **Decoding:** Converts IDs back to text.

### Code Example

```python
from transformers import GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
text = "I love Python and transformers!"
tokens = tokenizer.tokenize(text)
token_ids = tokenizer.convert_tokens_to_ids(tokens)
decoded_text = tokenizer.decode(token_ids)

print("Tokens:", tokens)
print("Token IDs:", token_ids)
print("Decoded Text:", decoded_text)
```

## Types of Tokenization

- **Word-level:** Splits by words.
- **Subword-level:** Splits by subwords (used by GPT-2).
- **Character-level:** Splits by characters.

GPT-2 uses **Byte Pair Encoding (BPE)**, which breaks words into subword units to handle unknown words efficiently.

## Byte Pair Encoding (BPE) Explained

**Byte Pair Encoding (BPE)** is a subword tokenization algorithm. It starts by splitting text into individual characters and then iteratively merges the most frequent pairs of characters or character sequences to form new subword units. This process continues until a predefined vocabulary size is reached.

### Why BPE?

- **Handles rare and unknown words:** By breaking words into subword units, BPE can represent words not seen during training.
- **Reduces vocabulary size:** Instead of storing every possible word, BPE stores common subwords, making the model more memory-efficient.
- **Improves generalization:** The model can understand and generate new words by combining known subwords.

### BPE Example

Suppose you have the words:  
`low`, `lowest`, `newer`, `wider`

1. **Initial split:**  
   Each word is split into characters:  
   `l o w`, `l o w e s t`, `n e w e r`, `w i d e r`

2. **Count pairs:**  
   Find the most frequent adjacent pairs (e.g., `l o`, `o w`, `w e`, etc.).

3. **Merge most frequent pair:**  
   If `l o` is most frequent, merge to `lo`:  
   `lo w`, `lo w e s t`, `n e w e r`, `w i d e r`

4. **Repeat:**  
   Continue merging frequent pairs (e.g., `lo w` → `low`, `e r` → `er`).

5. **Result:**  
   Common subwords like `low`, `est`, `new`, `er`, `wid` are created.

### BPE in GPT-2

GPT-2 uses BPE to tokenize text, allowing it to efficiently process and generate words, including those it has never seen before.

### Other Tokenization Algorithms

Besides Byte Pair Encoding (BPE), tokenizers use several other algorithms:

#### 1. WordPiece

- Used by models like BERT.
- Similar to BPE, but uses a different strategy for merging subwords based on likelihood.
- Example:  
  The word "unhappiness" might be split into `["un", "##happi", "##ness"]`.

#### 2. Unigram Language Model

- Used by models like XLNet and SentencePiece.
- Builds a vocabulary of subwords based on probability, not frequency.
- Example:  
  The word "internationalization" might be split into `["international", "ization"]`.

#### 3. Character-level Tokenization

- Splits text into individual characters.
- Useful for languages with large character sets or for tasks needing fine granularity.
- Example:  
  "hello" → `["h", "e", "l", "l", "o"]`

#### 4. Word-level Tokenization

- Splits text by whitespace or punctuation.
- Simple, but cannot handle unknown words or misspellings well.
- Example:  
  "I love Python!" → `["I", "love", "Python", "!"]`

#### 5. SentencePiece

- Can use BPE or Unigram algorithms.
- Treats input as a raw stream of characters, allowing language-agnostic tokenization.
- Example:  
  "tokenization" → `["token", "ization"]` or `["to", "ken", "ization"]`

Each algorithm has trade-offs in vocabulary size, handling of unknown words, and efficiency. Modern models often use subword tokenization (BPE, WordPiece, Unigram) for flexibility and robustness.
