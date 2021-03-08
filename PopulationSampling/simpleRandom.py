import random


class Sample:

    @staticmethod
    def simpRandSamp(seed, nums, data):
        random.seed(seed)
        return ListPick.listPickListSeed(seed, nums, data)
