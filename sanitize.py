import ast

class StringRemover(ast.NodeTransformer):
    def visit_FunctionDef(self,node): # We will override this method
        self.generic_visit(node)  # Recursively process nested functions 

        new_body = []
        for statment in node.body:
            if (isinstance(statment,ast.Expr) and isinstance(statment.value,ast.Constant) and isinstance(statment.value.value,str)):
                continue

            new_body.append(statment)

        node.body = new_body

        return node       
    




    def sanitize(code:str)->str:
        try:
            tree = ast.parse(code)
        except SyntaxError:
            raise ValueError("Error: This tool only generates unit tests for functions.")   


        tranformer = StringRemover()
        cleaned_tree = tranformer.visit(tree) 

        return ast.unparse(cleaned_tree)