"""
Exercise some the examples to make sure they're doing what we expect.
"""
import unittest
from zope.interface.exceptions import BrokenImplementation, Invalid

from expression import *
from binary_search import *

class ExpressionTest(unittest.TestCase):

    def test_integer_node(self):
        life_universe = IntegerExpressionNode(42)
        self.assertEqual(42, life_universe.evaluate())


    def test_broken_integer_node(self):
        """ 
        Make sure the BrokenIntegerExpressionNode behaves
        correctly even though it's not providing the interface that it
        claims to provide.  
        """
        life_universe = BrokenIntegerExpressionNode(42)
        self.assertEqual(42, life_universe.evaluate())


    def test_addition_node(self):
        twenty_one = AdditionExpressionNode(IntegerExpressionNode(10), IntegerExpressionNode(11))
        self.assertEqual(21, twenty_one.evaluate())


    def test_validate_addition_node(self):
        self.assertIsNone(validate_addition_node())

    
    def test_validate_integer_node(self):
        self.assertIsNone(validate_integer_node())


    def test_validate_broken_integer_node(self):
        self.assertRaises(BrokenImplementation, validate_broken_integer_node)


class AscendingListTest(unittest.TestCase):
    
    def test_verify_ascending_list(self):
        self.assertIsNone(verify_ascending_list())


    def test_verify_nonascending_list(self):
        self.assertIsNone(verify_nonascending_list())


    def test_validate_ascending_list(self):
        self.assertIsNone(validate_ascending_list())

    
    def test_validate_nonascending_list(self):
        self.assertRaises(Invalid, validate_nonascending_list)


if __name__ == "__main__":
    unittest.main()
