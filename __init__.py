#!/usr/bin/env python3

"""
An abstraction layer to make precomputing all technical indicators
and oscillators easier, keep a database and dataframes of historical
precomputes synchronized, and form algorithms for two to six week
trading cycles.
"""

from .pystock import Abstractions
from .stockDbSync import ManageTickers
from .PandasTALib import Abstract
from .Analysis import Analysis
import talib

#pylint thinks these are constants...  idiotic, it ends in parens
#and is cased to represent a class instance....
#obviously not a constant, but an instance.

manage_tickers = ManageTickers()
abstract = Abstractions(manage_tickers)
#I didn't want to do this, but I had to...
ta = Abstract(abstract, talib.abstract.__FUNCTION_NAMES)
abstract.ta = ta
