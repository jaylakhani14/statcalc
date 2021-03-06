class Mean:

    @staticmethod
    def mean(num):
        sum = 0
        for i in num:
            sum = sum + i
        return sum / len(num)