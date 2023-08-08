##

## Endpoint Signatures

Each endpoint has a signature. This means either a `GET` or `POST` request followed by the URI. Below is an example of the Completions endpoint signature. It uses a `POST` method. Other signatures may require a parameter. These will be identified by curly brackets `{ }`.

|||info
## Completions Endpoint Signature

```markdown-hide-clipboard
POST https://api.openai.com/v1/completions
```
|||

Endpoint signatures are provided in the examples below to give you a better idea of how the OpenAI is doing behind the scenes.


## List Model Endpoint

|||info
## List Model Endpoint Signature

```markdown-hide-clipboard
GET https://api.openai.com/v1/models
```
|||


This code prints out a long list of all of the available models and accompanying metadata. You can see why this is sometimes referred to as the metadata endpoint.

```python 
models = openai.Model.list()
print(models)
```

{Try It!}(python3 temp.py 1)

In a previous discussion, we talked about the four different types of models: `davinci`, `curie`, `babbage`, and `ada`. Each of these models varies in terms of capabilities, speed, and cost. However, the list of available models is greater than four. We will see later how we can use models like `text-search-babbage-query-001`.

Printing all of the models looks like it may be a JSON object or a dictionary. In reality, the return type from the API call is `OpenAIObject`. However, we can treat it like a dictionary. The code below prints out the first model and its metadata.

```python 
models = openai.Model.list()
print(models["data"][0])
```

{Try It!}(python3 temp.py 2)

|||challenge
## Try this variation:
* Create a list of all the model IDs without any other metadata.

```python
models = openai.Model.list()
model_ids = [model["id"] for model in models["data"]]
print(model_ids)
```

{Try It!}(python3 temp.py 3)
|||


## Retrieve Model Endpoint 

|||info
## List Engines Endpoint Signature

```markdown-hide-clipboard
GET https://api.openai.com/v1/models/{model}
```
|||

Instead of parsing the list of models, you can retrieve metadata about a specific one if you know the `id` for the model. The code sample below prints out the metadata for the `text-davinci-002` model.

```python
model = openai.Model.retrieve("text-davinci-002")
print(model)
```

{Try It!}(python3 temp.py 4)

{Check It!|assessment}(multiple-choice-95806836)
