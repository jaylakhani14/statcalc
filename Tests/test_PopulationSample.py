import unittest

from PopulationSampling.simpleRandom import Sample

class MyTestCase(unittest.TestCase):
    def test_simple_random_sample(self):
        mylist = ["apple", "banana", "cherry"]
        Sample.sample(mylist,2)

if __name__ == '__main__':
    unittest.main()