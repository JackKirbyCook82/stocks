# -*- coding: utf-8 -*-
"""
Created on Sun Jul 5 2026
@name:   Stock Objects
@author: Jack Kirby Cook

"""

import pandas as pd
from types import NoneType

from finance.variables import Enumerations
from finance.logging import Logging
from support.equations import Equations

__version__ = "1.0.0"
__author__ = "Jack Kirby Cook"
__all__ = ["StockCalculator"]
__copyright__ = "Copyright 2026, Jack Kirby Cook"
__license__ = "MIT License"


class StockCalculator(Logging, Equations):
    mean = lambda bid, ask, supply, demand: ((bid * demand) + (ask * supply)) / (demand + supply)
    median = lambda bid, ask: (bid + ask) / 2
    gap = lambda bid, ask: ask - bid

    def __call__(self, stocks, technicals=None, /, **kwargs):
        assert isinstance(stocks, pd.DataFrame)
        assert isinstance(technicals, (pd.DataFrame, NoneType))
        if technicals is not None: stocks = self.merge(stocks, technicals, **kwargs)
        calculated = self.execute(stocks, **kwargs)
        stocks = pd.concat([stocks, calculated], axis=1)
        self.results(stocks, title="Calculated", instrument=Enumerations.Instrument.STOCK)
        return stocks

    @staticmethod
    def merge(stocks, technicals, /, **kwargs):
        technicals = technicals[technicals["date"] <= pd.Timestamp.today()]
        technicals = technicals.sort_values(["ticker", "date"]).groupby("ticker", as_index=False).last()
        technicals = technicals[["ticker", "date", "volatility", "trend"]]
        stocks = stocks.merge(technicals, on="ticker", how="left")
        return stocks




