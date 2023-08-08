##

So far, we have interacted with the GPT-3 model by using the official [OpenAI playground](https://beta.openai.com/playground), a text file for our prompts, or an IDE with some Python code. The user interfaces for these methods of interaction are all different. However, all of these interactions are making use of API endpoints.

An endpoint for the OpenAI API is a uniform resource identifier (URI) that is used to access data or services provided by the company. Each endpoint represents a different way of interacting with OpenAI. Send information to a specific endpoint, and OpenAI sends back a response based on your initial query.

All of our examples up until now have used the Completions endpoint when generating a response to our prompts. This is one of several endpoints available to users. Here is the full list of available endpoints:

1. **List Models** - also known as the metadata endpoint; returns a list of models as well as some metadata about each model
2. **Retrieve Model** - returns detailed metadata about the specified model
3. **Completions** - most popular endpoint; returns a response to a prompt
4. **Semantic Search** - allows you to semantically rank documents with natural language
5. **Files** - upload and manipulate files in OpenAI storage
6. **Classification** - lets you classify a query without the need for finetuning or hyperparameter tuning
7. **Answers**  - takes a question and returns an answer based on provided information (files or training examples)
8. **Embeddings** - returns an embedding based on information sent to the API

We will be exploring some of these endpoints throughout this assignment. OpenAI is actively working on new engines and updating existing ones. Over time, there might be some changes to the endpoints we see now.

{Check It!|assessment}(multiple-choice-1672587686)
