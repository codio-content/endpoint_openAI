##

## Embedding Endpoint

|||info
## Embeddings Endpoint Signature

```markdown-hide-clipboard
POST https://api.openai.com/v1/embeddings
```
|||

The API also has another experimental endpoint called *embeddings*. Embeddings are a representation of a given input as a vector of floating point numbers. Embeddings can be easily consumed by machine learning models and algorithms. They are often used to determine the semantic similarity between two texts. If two texts are similar, then their vector representations should also be similar.

Currently OpenAI offers three families of embedding models that allow for text search, text similarity and code search. Each family includes up to four models on a spectrum of capabilities:

* **Ada** (1024 dimensions),
* **Babbage** (2048 dimensions),
* **Curie** (4096 dimensions),
* **Davinci** (12288 dimensions).

These embedding models are specifically created to be good at a particular task. For example, `text-similarity-ada-001` is good at capturing semantic similarity between two or more pieces of text. Or `text-search-ada-doc-001` helps measure whether long documents are relevant to a short search query. For more information on embeddings, see the OpenAI [documentation](https://beta.openai.com/docs/guides/embeddings).

## Creating an Embedding

In this example, we are going to use the `text-similarity-babbage-001` model. We also need to provide some text for the embedding. This is done with the `input` keyword argument. Both of these are required. The `user` keyword argument is optional. This unique identifier can be used to help monitor for abuse. The code sample below should print a long list of floating point numbers.

```python
emb=openai.Embedding.create(
  model="text-similarity-babbage-001",
  input="You will rejoice to hear that no disaster has accompanied the")

print(emb)
```

{Try it!}(python3 embedding.py 1)

Just like the list of models, the return object is of type `OpenAIObject`. If you want to access just the vector, change the print statement to the following:

```python
print(emb["data"][0]["embedding"])
```

{Try it!}(python3 embedding.py 2)



{Check It!|assessment}(multiple-choice-3943586042)
