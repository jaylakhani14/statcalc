import unittest
from RandomGenerator.randNum import RandNum
from RandomGenerator.randList import RandList
from RandomGenerator.listPick import ListPick

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.test = [0, 1, 2, 3, 4]

    def test_randNum(self):
        result = RandNum.randNum(0, 5)
        self.assertEqual(int, type(result))

    def test_randNumSeed(self):
        result1 = RandNum.randNumSeed(5, 0, 20)
        result2 = RandNum.randNumSeed(5, 0, 20)
        self.assertEqual(True, result1 == result2)

    def test_randFloat(self):
        result = RandNum.randFloat(0, 10)
        self.assertEqual(float, type(result))

    def test_randFloatSeed(self):
        result1 = RandNum.randFloatSeed(5, 0, 20)
        result2 = RandNum.randFloatSeed(5, 0, 20)
        self.assertEqual(True, result1 == result2)

    def test_randNumList(self):
        result1 = RandList.randList(1, 5, 0, 5)
        result2 = RandList.randList(1, 5, 0, 5)
        self.assertEqual(True, result1 == result2)

    def test_randFloatList(self):
        result1 = RandList.randList(1, 5, 0, 5)
        result2 = RandList.randList(1, 5, 0, 5)
        self.assertEqual(True, result1 == result2)

    def test_listPick(self):
        result = ListPick.listPick(self.test)
        x = None
        if result in self.test and type(result) == int:
            x = True
        self.assertEqual(True, x)

    def test_listPickSeed(self):
        result = ListPick.listPickSeed(3, self.test)
        result2 = ListPick.listPickSeed(3, self.test)
        x = None
        if result in self.test and type(result) == int:
            if result == result2:
                x = True
        self.assertEqual(True, x)

    def test_listPickList(self):
        temp = ListPick.listPickList(2, self.test)
        x = None
        if len(temp) == 2:
            for item in temp:
                if item in self.test and type(item) == int:
                    x = True
        self.assertEqual(True, x)

    def test_listPickListSeed(self):
        temp = ListPick.listPickListSeed(5, 2, self.test)
        temp2 = ListPick.listPickListSeed(5, 2, self.test)
        x = None
        if temp == temp2:
            x = True
        self.assertEqual(True, x)


if __name__ == '__main__':
    unittest.main()