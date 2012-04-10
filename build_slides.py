import sys
import ast
from unparse import Unparser

def get_slide_name(slide_str):
    return ":".join(slide_str.split(":")[1:]).strip()

class SlideVisitor(ast.NodeVisitor):
    
    slide_nodes = {}
    recording = False
    slide_name = None

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
    

if __name__ == "__main__":
    filename = "test_file.py"
    with open(filename) as source_file:        
        source = source_file.read()
        tree = compile(source, filename, "exec", ast.PyCF_ONLY_AST)
        visitor = SlideVisitor()
        visitor.visit(tree)
        for slide_name, node in visitor.slide_nodes.iteritems():
            #print ast.dump(node)
            Unparser(node, sys.stdout)
            print "\n"
            print "*"*80
    
