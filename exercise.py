import openai
import secret
openai.api_key=secret.api_key

def fix_spelling(text: str) -> str:
  #please put your code below this line

### CODIO SOLUTION BEGIN
    edi = openai.Edit.create(
        model="text-davinci-edit-001",
        input=text,
        instruction="Fix the spelling mistakes"
    )
    return edi['choices'][0]['text'].strip()
### CODIO SOLUTION END

# FREEZE CODE BEGIN
input_texts = [
    "I hve a bananna for brekfast.",
    "The colur of the sky is rde.",
    "The grass is greneer on the other side."
]

for input_text in input_texts:
    output_text = fix_spelling(input_text)
    print(f"Input: {input_text}\nOutput: {output_text}\n")
# FREEZE CODE END