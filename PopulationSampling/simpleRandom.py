import random


class Sampling:

    @staticmethod
    def simple(sequence, k):
        return random.sample(sequence, k)
