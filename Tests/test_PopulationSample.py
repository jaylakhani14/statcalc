import unittest

import numpy as np
import scipy

from PopulationSampling.simpleRandom import Sample
from PopulationSampling.confidence import Confidence


class MyTestCase(unittest.TestCase):
    def test_simple_random_sample(self):
        mylist = ["apple", "banana", "cherry"]
        Sample.sample(mylist, 2)

    def test_confidence_interval(self):
        sample = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        c = 0.95
        df = len(sample) - 1
        sample_mean = np.mean(sample)
        sample_standard_error = scipy.stats.sem(sample)
        Confidence.mean_confidence_interval(c, df, sample_mean, sample_standard_error)


if __name__ == '__main__':
    unittest.main()
