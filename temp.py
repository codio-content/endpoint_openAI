import os
import openai
import secret
openai.api_key=secret.api_key

### CODIO SOLUTION BEGIN
model = openai.Model.retrieve("text-davinci-002")
print(model)
### CODIO SOLUTION END