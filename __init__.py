# -*- coding: utf-8 -*-
"""
Created on Sun Jul 5 2026
@name:   Stock Objects
@author: Jack Kirby Cook
@file:   stocks/__init__.py

"""

import pandas as pd

from support.equations import DataframeEquation
from support.mixins import Logging

__version__ = "1.0.0"
__author__ = "Jack Kirby Cook"
__all__ = ["StockCalculator"]
__copyright__ = "Copyright 2026, Jack Kirby Cook"
__license__ = "MIT License"


class StockCalculator(DataframeEquation, Logging):
    mean = lambda bid, ask, supply, demand: ((bid * demand) + (ask * supply)) / max(demand + supply).clip(lower=1e-10)
    median = lambda bid, ask: (bid + ask) / 2

    def __call__(self, stocks, /, **kwargs):
        if stocks is None: return None
        assert isinstance(stocks, pd.DataFrame)
        if stocks.empty: return None
        calculated = self.execute(stocks, **kwargs)
        stocks = pd.concat([stocks, calculated], axis=1)
        return stocks



