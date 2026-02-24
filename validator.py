import ast

def single_def_validator(code:str):
    try:
        tree = ast.parse(code)

    except ValueError:
        raise ValueError("Error: This tool only generates unit tests for functions.")

    function = [node for node in tree.body if isinstance(node,ast.FunctionDef)]

    if len(function) != 1 :
        raise ValueError("Error: This tool only generates unit tests for functions.")
    else:
        return function[0]  

      