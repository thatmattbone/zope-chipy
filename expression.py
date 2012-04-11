from zope.interface import implementer, Interface, Attribute
from zope.interface.verify import verifyObject

"""SLIDE_START: define_interface"""

class IExpressionNode(Interface):
    left = Attribute("The left child of this expression.")
    right = Attribute("The right child of this expression.")

    def evaluate():
        """Evaluate this expression"""

"""SLIDE_END: define_interface"""


"""SLIDE_START: addition_expression_node"""
@implementer(IExpressionNode)
class AdditionExpressionNode(object):

    def __init__(self, left, right):
        self.left = left
        self.right = right


    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate()
"""SLIDE_END: addition_expression_node"""

@implementer(IExpressionNode)
class IntegerExpressionNode(object):
    
    left = None
    right = None
    
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value


@implementer(IExpressionNode)
class BrokenIntegerExpressionNode(object):
        
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value

"""SLIDE_START: validate_addition_node"""
def validate_addition_node():
    
    five = IntegerExpressionNode(5)
    three = IntegerExpressionNode(3)
    eight = AdditionExpressionNode(five, three)

    IExpressionNode.implementedBy(AdditionExpressionNode)
    IExpressionNode.providedBy(eight)
    verifyObject(IExpressionNode, eight)
"""SLIDE_END: validate_addition_node"""


def validate_integer_node():
    IExpressionNode.implementedBy(IntegerExpressionNode)
    eight = IntegerExpressionNode(8)
    IExpressionNode.providedBy(eight)
    verifyObject(IExpressionNode, eight)


def validate_broken_integer_node():
    IExpressionNode.implementedBy(BrokenIntegerExpressionNode)
    eight = BrokenIntegerExpressionNode(8)
    IExpressionNode.providedBy(eight)
    verifyObject(IExpressionNode, eight)

