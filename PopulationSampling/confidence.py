import numpy as np
import scipy.stats


class Confidence:

    @staticmethod
    def mean_confidence_interval(confidence_level, degrees_freedom, sample_mean, sample_standard_error):
        c = confidence_level
        df = degrees_freedom
        s = sample_mean
        sstde = sample_standard_error
        print(scipy.stats.t.interval(c, df, s, sstde))