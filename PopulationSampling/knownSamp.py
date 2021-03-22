from DescriptiveStatictics.zscore import zscore
from PopulationSampling.marginoferror import marginoferror
from DescriptiveStatictics.std import std
from MathOperations.exponent import exponent


class knownSamp:
    @staticmethod
    def knownSamplesize(seed, data):
        z = Zsc.zscore(seed, data)
        Mar = MarginOfError.marginoferror(seed, data)
        Std = Stddev.std(data)
        value = (z * Std) / Mar
        sam = Exponent.power(value, 2)
        return sam
