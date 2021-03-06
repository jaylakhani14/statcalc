import unittest

from Calculator.Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_calculator_return_sum(self):
        result = self.calculator.Sum(1, 2)
        self.assertEqual(3, result)

    def test_calculator_access_sum_result(self):
        self.calculator.Sum(1, 2)
        self.assertEqual(3, self.calculator.Result)

    def test_calculator_return_difference(self):
        result = self.calculator.Difference(1, 2)
        self.assertEqual(-1, result)

    def test_calculator_access_difference_result(self):
        self.calculator.Difference(1, 2)
        self.assertEqual(-1, self.calculator.Result)

    def test_calculator_return_product(self):
        result = self.calculator.Multiplication(1, 2)
        self.assertEqual(2, result)

    def test_calculator_access_product_result(self):
        self.calculator.Multiplication(1, 2)
        self.assertEqual(2, self.calculator.Result)

    def test_calculator_divide(self):
        result = self.calculator.Divide(10, 5)
        self.assertEqual(2, result)

    def test_calculator_root(self):
        result = self.calculator.Root(9)
        self.assertEqual(3, result)

    def test_calculator_power(self):
        result = self.calculator.Power(4,2)
        self.assertEqual(16, result)

    def test_calculator_log(self):
        result = self.calculator.Logarithm(10, 1)
        self.assertEqual(0, result)


if __name__ == '__main__':
    unittest.main()