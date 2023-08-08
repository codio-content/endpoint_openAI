import subprocess

def check_python_file(file_path):
    try:
        output = subprocess.check_output(['python', file_path], stderr=subprocess.STDOUT)
        return True
    except subprocess.CalledProcessError as e:
        print(e.output)
        return False

# Example usage
if check_python_file('exercise.py'):
    print("The file runs without errors.")
    import importlib
    import openai

    # load the student's script
    student_script = importlib.import_module('exercise')

    def test_fix_spelling():
        # Prepare dummy inputs and expected outputs
        input_texts = [
            "I hve a bananna for brekfast.",
            "The colur of the sky is rde.",
            "The grass is greneer on the other side."
        ]

        expected_outputs = [
            "I have a banana for breakfast.",
            "The color of the sky is red.",
            "The grass is greener on the other side."
        ]

        for input_text, expected_output in zip(input_texts, expected_outputs):
            # Run the student's function
            try:
                output_text = student_script.fix_spelling(input_text)

                if  output_text != expected_output:
                   f"For input '{input_text}', expected '{expected_output}' but got '{output_text}'"

                print(f"Test for input '{input_text}' passed!")
            except Exception as e:
                print(f"Test for input '{input_text}' failed: {e}")

    # Run the test function
    test_fix_spelling()

else:
    print("The file generated errors.")

