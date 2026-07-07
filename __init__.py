# -*- coding: utf-8 -*-
"""
Created on Sun Jul 5 2026
@name:   Stock Objects
@author: Jack Kirby Cook

"""

import numpy as np
import pandas as pd

from finance.variables import Enumerations
from finance.logging import Logging
from support.equations import Equations

__version__ = "1.0.0"
__author__ = "Jack Kirby Cook"
__all__ = ["StockCalculator"]
__copyright__ = "Copyright 2026, Jack Kirby Cook"
__license__ = "MIT License"


class StockCalculator(Logging, Equations):
    quality = lambda activity, tightness: activity / (tightness ** 2 + 1e-6)
    activity = lambda supply, demand: np.minimum(supply, demand) / (np.maximum(supply, demand) + 10)
    tightness = lambda gap, median: gap / median
    mean = lambda bid, ask, supply, demand: ((bid * demand) + (ask * supply)) / (demand + supply)
    median = lambda bid, ask: (bid + ask) / 2
    gap = lambda bid, ask: ask - bid

    def __call__(self, stocks, /, **kwargs):
        assert isinstance(stocks, pd.DataFrame)
        calculated = self.execute(stocks, **kwargs)
        stocks = pd.concat([stocks, calculated], axis=1)
        self.results(stocks, title="Calculated", instrument=Enumerations.Instrument.STOCK)
        return stocks



