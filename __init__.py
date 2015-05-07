from .pystock import Abstractions
from .stockDbSync import ManageTickers
from .PandasTALib import Abstract
from .Analysis import Analysis
import talib
manage_tickers = ManageTickers()
abstract = Abstractions(manage_tickers)
ta = Abstract(abstract, talib.abstract.__FUNCTION_NAMES)
abstract.ta = ta
