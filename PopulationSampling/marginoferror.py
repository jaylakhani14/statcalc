from DescriptiveStatisctics.zscore import zscore
from DescriptiveStatistics.std import std

class MarginOfError:
    @staticmethod
    def marginoferror(seed, data):
        zscore = Zscore.zscore(seed, data)
        std = Std.std(data)
        return zscore * std