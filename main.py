from validator import single_def_validator
from sanitize import StringRemover
import ast
import sys
from llm_client import LLMClient
import pathlib

def read_source_from_file():
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_python_file>")
        sys.exit(1)

    file_path = pathlib.Path(sys.argv[1])

    if not file_path.exists():
        print("Error: File does not exist.")
        sys.exit(1)

    return file_path.read_text()


user_input = read_source_from_file()
function = single_def_validator(user_input)
clean_function = StringRemover.sanitize(ast.unparse(function))

llm = LLMClient()
print(llm.generate(clean_function))