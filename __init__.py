# -*- coding: utf-8 -*-
"""
Created on Sun Jul 5 2026
@name:   Stock Objects
@author: Jack Kirby Cook
@file:   stocks/__init__.py

"""

import pandas as pd

from finance.enumerations import Instrument
from finance.reporting import Results
from support.equations import Equations
from support.mixins import Logging

__version__ = "1.0.0"
__author__ = "Jack Kirby Cook"
__all__ = ["StockCalculator"]
__copyright__ = "Copyright 2026, Jack Kirby Cook"
__license__ = "MIT License"


class StockCalculator(Results, Logging, Equations):
    mean = lambda bid, ask, supply, demand: ((bid * demand) + (ask * supply)) / (demand + supply)
    median = lambda bid, ask: (bid + ask) / 2

    def __call__(self, stocks, /, **kwargs):
        assert isinstance(stocks, pd.DataFrame)
        scope = self.scope(stocks, instrument=Instrument.STOCK)
        calculated = self.execute(stocks, **kwargs)
        stocks = pd.concat([stocks, calculated], axis=1)
        results = self.results(scope=scope, size=len(stocks))
        self.console("Calculated", results)
        return stocks



