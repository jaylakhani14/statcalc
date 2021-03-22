import unittest
from random import random

from DescriptiveStatistics.mean import Mean
from DescriptiveStatistics.median import Median
from DescriptiveStatistics.mode import Mode
from DescriptiveStatistics.variance import Variance
from DescriptiveStatistics.std import Std
from DescriptiveStatistics.zscore import Zscore



class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.test = [1, 2, 3, 4, 5]
        self.test1 = [1, 2, 2, 3, 4]
        self.test2 = [1, 2, 3]
        self.test3 = [1, 2, 3, 4, 5, 6, 7]
        self.test4 = [1, 2, 3, 4, 5, 6]
        self.test5 = [1, 2, 3, 3, 3, 4, 5]

    def test_Mean(self):
        self.assertEqual(3, Mean.mean(self.test))

    def test_mode(self):
        self.assertEqual(2, Mode.mode(self.test1))

    def test_median(self):
        self.assertEqual(2, Median.median(self.test2))

    def test_variance(self):
        self.assertEqual(2, Variance.variance(self.test))

    def test_stddev(self):
        self.assertEqual(1.5811388300841898, Stddev.stddev(self.test))
        
    def test_zscore(self):
        self.assertEqual(Zscore.zscore(self.test3)


if __name__ == '__main__':
    unittest.main()
