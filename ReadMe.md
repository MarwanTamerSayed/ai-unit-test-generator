# ==============================
# README.md
# ==============================
echo "## Python CLI Unit Test Generator

A command-line tool that automatically generates Python unit tests for any given function using a Large Language Model (LLM).  
This project is built as a strict CLI developer tool, suitable for quickly producing test cases including normal, edge, and boundary cases.

---

## Features

- Accepts a Python function as input.
- Generates **comprehensive unit tests** with Python \`unittest\`.
- Handles nested functions.
- Sanitizes the function and removes docstrings to prevent prompt injection.
- Supports multiple free LLM endpoints via OpenRouter.
- Warns when using free models and allows partial output if the model fails strict validation.

---

## Requirements

- Python 3.11+
- Install dependencies:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

- Create a \`.env\` file with your OpenRouter credentials:

\`\`\`
OPENROUTER_API_KEY=<your_api_key>
OPENROUTER_BASE_URL=https://api.openrouter.ai/v1
OPENROUTER_MODEL=qwen/qwen-3-coder:free
\`\`\`

---

## Usage

###  Read function from a file

\`\`\`bash
python main.py path/to/your_file.py
\`\`\`

The script will read the function from the file and generate the corresponding unit tests.

---

## Example

Input function:

\`\`\`python
def add(a, b):
    return a + b
\`\`\`

Generated unit tests (partial):

\`\`\`python
import unittest

class TestAddFunction(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(5, 6), 11)

    def test_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)
\`\`\`

---

## Notes

- Free LLM models may return **incomplete or slightly incorrect output**.  
  The program will warn you if that happens:
  
\`\`\`
[WARN] The generated unit tests may be incomplete or not fully correct because this is a free model. Please review manually.
\`\`\`

- The tool **never exposes your API key**. Make sure your \`.env\` file is in \`.gitignore\`.

---

## Project Structure

\`\`\`
ai_test_generator/
│
├─ main.py           # CLI entry point
├─ validator.py      # Validates input function
├─ sanitizer.py      # Cleans source code / removes docstrings
├─ llm_client.py     # LLM API wrapper
├─ requirements.txt  # Dependencies
├─ .env              # API key (ignored in git)
└─ README.md
\`\`\`

---

## License

MIT License
" > README.md

# ==============================
# .gitignore
# ==============================
echo ".env
__pycache__/
*.pyc
*.pyo
*.pyd
.env
.vscode/
" > .gitignore

# ==============================
# requirements.txt
# ==============================
echo "python-dotenv
openai
" > requirements.txt
