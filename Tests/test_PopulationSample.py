import unittest

import numpy as np
import scipy

from PopulationSampling.simpleRandom import Sample
from PopulationSampling.confidence import Confidence

class MyTestCase(unittest.TestCase):
    def test_simple_random_sample(self):
        mylist = ["apple", "banana", "cherry"]
        Sample.sample(mylist,2)

if __name__ == '__main__':
    unittest.main()