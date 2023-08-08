Using the OpenAI Edit API, create a Python function `fix_spelling` that takes a string as input and returns a corrected version of the input with spelling mistakes fixed. The function should use the `text-davinci-edit-001` model. For a more effective output make `top_p`=0.1 as one of your arguments.

{Try it!}(python3 exercise.py)

{Check It!|assessment}(code-output-compare-907671071)
|||guidance
import openai
import secret
openai.api_key=secret.api_key

def fix_spelling(text: str) -> str:
    edi = openai.Edit.create(
        model="text-davinci-edit-001",
        input=text,
        instruction="Fix the spelling mistakes",
        top_p=0.1
    )
    return edi['choices'][0]['text'].strip()


# FREEZE CODE BEGIN
input_texts = [
    "I hve a bananna for brekfast.",
    "The colur of the sky is blu.",
    "The grass is greneer on the other side."
]

for input_text in input_texts:
    output_text = fix_spelling(input_text)
    print(f"Input: {input_text}\nOutput: {output_text}\n")
# FREEZE CODE BEGIN
|||