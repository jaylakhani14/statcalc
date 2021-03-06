from MathOperations.addition import Addition
from MathOperations.subtraction import Subtraction
from MathOperations.multiplication import Multiplication
from MathOperations.division import Division
from MathOperations.exponent import Exponent
from MathOperations.log import Log
from MathOperations.root import Root


class Calculator:
    Result = 0
    def __init__(self):
        pass
    def Sum(self, a, b):
        self.Result = Addition.sum(a, b)
        return self.Result

    def Difference(self, a, b):
        self.Result = Subtraction.difference(a, b)
        return self.Result

    def Multiplication(self, a, b):
        self.Result = Multiplication.multiplication(a, b)
        return self.Result

    def Divide(self, a, b):
        self.Result = Division.quotient(a, b)
        return self.Result

    def Root(self, a):
        self.Result = Root.sqr_root(a)
        return self.Result

    def Power(self, a, b):
        self.Result = Exponent.power(a, b)
        return self.Result

    def Logarithm(self, a, b):
        self.Result = Log.logarithm(a, b)
        return self.Result