from RandomGenerator.randNum import RandNum

class RandList:

    @staticmethod
    def randList(length, seed, lower, upper):
        data = []
        while len(data) != length:
            data.append(RandNum.randNumSeed(seed, lower, upper))
        return data

    @staticmethod
    def randListFloat(length, seed, lower,upper):
        data = []
        while len(data != length):
            data.append(RandNum.randFloatSeed(seed, lower, upper))