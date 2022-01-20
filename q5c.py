import ast
import inspect
import importlib
import glob
import os

class FunctionCounter(ast.NodeVisitor):
    function_count=0
            
    def visit_FunctionDef(self, node):
        self.function_count+=1
        
    # def visit_Lambda(self, node):
       # self.function_count +=1
        
if __name__ == '__main__':
    count=0
    directory = os.getcwd() + ('/my-python-project/**/*.py')
    python_files_list =glob.glob(directory, recursive=True);
    
    for filename in python_files_list:
        p=ast.parse(open(filename).read())
        f=FunctionCounter()
        f.visit(p)
        count += f.function_count

    print(count)
