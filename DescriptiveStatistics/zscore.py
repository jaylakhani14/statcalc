import pandas as pd
import numpy as np
import scipy.stats as stats

class Zscore:

    @staticmethod
    def zscore(num):
        return stats.zscore(num)
