import unittest

from MathOperations.addition import Addition
from MathOperations.subtraction import Subtraction
from MathOperations.multiplication import Multiplication
from MathOperations.division import Division
from MathOperations.exponent import Exponent
from MathOperations.log import Log
from MathOperations.root import Root


class MyTestCase(unittest.TestCase):

    def test_MathOperations_Addition(self):
        self.assertEqual(3, Addition.sum(1, 2))

    def test_MathOperations_subtraction(self):
        self.assertEqual(-1, Subtraction.difference(1, 2))

    def test_MathOperations_sum_list(self):
        valuelist = [1, 2, 3]
        self.assertEqual(6, Addition.sum(valuelist))

    def test_MathOperations_multiplication(self):
        self.assertEqual(2, Multiplication.multiplication(1, 2))

    def test_MathOperations_division(self):
        self.assertEqual(2, quotient(10, 5))

    def test_MathOperations_exponent(self):
        self.assertEqual(16,Exponent.power(4,2))

    def test_MathOperations_log(self):
        self.assertEqual(0, Log.logarithm(10,1))

    def test_MathOperations_root(self):
        self.assertEqual(3, Root.sqr_root(9))


if __name__ == '__main__':
    unittest.main()