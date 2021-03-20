from DescriptiveStatictics.zscore import zscore
from PopulationSampling.marginoferror import marginoferror
from MathOperations.exponent import exponent
from MathOperations.subtraction import subtraction
from DescriptiveStatictics.std import std

class sampleSize:
    @staticmethod
    def samplesize(seed, data):
        z = Zscore.zscore(seed, data)
        Margin = marginoferror.marginoferror(seed, data)
        Std = Std.std(data)
        value = (z * Std) / Margin
        ss = exponent.power(value, 2)
        return ss
