import sys
import ast
from unparse import Unparser
import StringIO
import os
import webbrowser

import jinja2


def get_slide_name(slide_str):
    return ":".join(slide_str.split(":")[1:]).strip()


class SlideVisitor(ast.NodeVisitor):
    
    def __init__(self):
        self.slide_nodes = {}
        self.recording = False
        self.slide_name = None


    def visit_Str(self, node):
        if node.s.startswith("SLIDE_START: "):
            self.recording = True
            self.slide_name = get_slide_name(node.s)

        elif node.s.startswith("SLIDE_END: "):
            self.recording = False
            self.slide_name = None


    def generic_visit(self, node):
        if self.recording and self.slide_name not in self.slide_nodes:
            self.slide_nodes[self.slide_name] = node
        else:
            for child_node in ast.iter_child_nodes(node):
                self.visit(child_node)
    

def get_slide_ast_dict(filename):
    """
    Given a python filename return a dict mapping the slide names to
    AST trees of the code contained inside those slides.
    """
    with open(filename) as source_file:        
        source = source_file.read()
        tree = compile(source, filename, "exec", ast.PyCF_ONLY_AST)
        visitor = SlideVisitor()
        visitor.visit(tree)
    return visitor.slide_nodes
        

def ast_map_to_source_map(ast_map, filename):
    code_map = {}
    for slide_name, node in ast_map.iteritems():
        output = StringIO.StringIO()
        Unparser(node, output)
        code_map[slide_name] = {'code': output.getvalue(),
                                'filename': filename}
    return code_map
    

def render_slides(template_name, context):
    loader = jinja2.FileSystemLoader(os.getcwd())
    env = jinja2.Environment(loader=loader)
    return env.get_template(template_name).render(**context)


if __name__ == "__main__":
    code_map = {}
    filenames = ["test_file.py", 
                 "binary_search.py", 
                 "expression.py"]
    for filename in filenames:
        ast_map = get_slide_ast_dict(filename)
        code_map.update(ast_map_to_source_map(ast_map, filename))

    rendered = render_slides("presentation/index.html", code_map)
    
    with open("presentation/index_rendered.html", "wb") as rendered_file:
        rendered_file.write(rendered)
    
    webbrowser.open("presentation/index_rendered.html")
    
