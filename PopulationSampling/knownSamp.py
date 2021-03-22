from DescriptiveStatictics.zsc import Zsc
from PopulationSampling.marginOfError import MarginOfError
from DescriptiveStatictics.stddev import Stddev
from MathOperations.exponent import Exponent


class KnownSampleSize:
    @staticmethod
    def knownSamplesize(seed, data):
        z = Zsc.zsc(seed, data)
        Mar = MarginOfError.marginOfError(seed, data)
        StDe = Stddev.stddev(data)
        value = (z * StDe) / Mar
        sam = Exponent.power(value, 2)
        return sam
