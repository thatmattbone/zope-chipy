from zope.interface import implementer, Interface, Attribute
from zope.interface.verify import verifyObject

class IExpressionNode(Interface):
    left = Attribute("The left child of this expression.")
    right = Attribute("The right child of this expression.")

    def evaluate():
        """Evaluate this expression"""


@implementer(IExpressionNode)
class AdditionExpressionNode(object):

    def __init__(self, left, right):
        self.left = left
        self.right = right


    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate()


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


def validate_addition_node():
    IExpressionNode.implementedBy(AdditionExpressionNode)
    eight = AdditionExpressionNode(IntegerExpressionNode(5), IntegerExpressionNode(3))
    IExpressionNode.providedBy(eight)
    verifyObject(IExpressionNode, eight)


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

