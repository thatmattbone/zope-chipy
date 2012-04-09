from zope.interface import implementer, Interface, Attribute


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

