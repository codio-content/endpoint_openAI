### Edits
Given a prompt and an instruction, the model will return an edited version of the prompt.

`POST https://api.openai.com/v1/edits`
```python

edi= openai.Edit.create(
  model="text-davinci-edit-001",
  input="What day was it? Wesdneday?",
  instruction="Fix the spelling mistakes"
)
print(edi['choices'][0]['text'].strip())


```
{try it!}(python3 edits.py)


### The Edit body
Similarly to our create call our edit calls can take a couple of arguments to help the user better control what is generated. 

|||
The must-have arguments are `model` and `instruction`. 
```python
edi= openai.Edit.create(
  model="text-davinci-edit-001",
  instruction="Captitalize the first letter of all the words in the sentence"
)
print(edi['choices'][0]['text'].strip())
```
{try it!}(python3 edits.py 6)
For our purposes we are also going to make input as a default because it keeps it clean about what is the input we are interacting with. 

`input` : is optional but defaults to an empty string when no argument is specified. It is used  as a starting point for the edit.  
`instruction`: is required and tell the AI how to edit the prompt
|||

``` python
edi= openai.Edit.create(
  model="text-davinci-edit-001",
  input="What day was it? Wesdneday?",
  instruction="change wednesday to saturday."
)
print(edi['choices'][0]['text'].strip())
```
{try it!}(python3 edits.py 3)
Feel free to try it more than once, there might be a chance the AI misinterprets the directions.
Similarly, to create a call there are a couple of other optional arguments. In this case, we could have added `n`, `temperature` and `top_p`.

`n`: defaults to 1 and tells how many edits to create from input and instruction
`temperature`: defaults to 1 , higher values mean the model will take more risks.
`top_p`: 0.1 means only the tokens comprising the top 10% probability mass are considered.

A Try It button is provided in case you wanted to try adding some of those variables. 

{try it!}(python3 edits.py 4)
{Check It!|assessment}(multiple-choice-2404192563)


