import random

class RandNum:

    @staticmethod
    def randNum(lower, upper):
        return random.randint(lower, upper)

    @staticmethod
    def randNumSeed(seed,lower,upper):
        random.seed(seed)
        return RandNum.randNum(lower,upper)

    @staticmethod
    def randFloat(lower,upper):
        return random.uniform(lower,upper)

    @staticmethod
    def randFloatSeed(seed,lower,upper):
        random.seed(seed)
        return RandNum.randFloat(lower,upper)