import os
import openai
import secret
openai.api_key=secret.api_key

### CODIO SOLUTION BEGIN
edi= openai.Edit.create(
  model="text-davinci-edit-001",
  input="What day was it? Wesdneday?",
  instruction="change wednesday to saturday."
)
print(edi['choices'][0]['text'].strip())
### CODIO SOLUTION END