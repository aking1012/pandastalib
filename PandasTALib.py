'''
It seems a little like a useless re-implementation.  However, the point is that
I wanted an API that consisted of default arguments (existed), just throwing a
pandas series/df at a call (did not exist per se), and organized functions (did
not exist...  they were all top-level functions).

So, just simplifying, organizing, and documenting.

In the example.py there should be sample usage for every single
function eventually.
'''

import talib

#TODO add default values to each call and put in the df splitting/joining logic
#   for the same.
#   ...partially complete
#Add a brief explanation of each indicator/other to the docstring for the
#   indicator/other.  Think, the about/explanation from chartschool.com.
#Add examples to example.py

#Done
class CategoryTemplate:
    def __init__(self, tapandascompat):
        self.compat = tapandascompat

#TODO
class Momentum(CategoryTemplate):
    '''
    All momentum indicators reside here.
    '''
    def __init__(self, tapandascompat):
        super().__init__(tapandascompat)

    def ADX(self, df, timeperiod=-2**31):
        '''
        Average Directional Movement Index
        '''
        npa_result = talib.ADX(open = df['Open]',
                    high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    volume = df['Volume'],
                    timeperiod = timeperiod)
        df[pattern] = npa_result.tolist()
        return df

    def ADXR(self, df, timeperiod=-2**31):
        '''
        Average Directional Movement Index Rating
        '''
        npa_result = talib.ADX(open = df['Open]',
                    high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    volume = df['Volume'],
                    timeperiod = timeperiod)
        df[pattern] = npa_result.tolist()
        return df

    def APO(self, df, key='close', fastperiod=-2**31 , slowperiod=-2**31 , matype=0):
        '''
        Absolute Price Oscillator
        '''
        npa_result = talib.ADX(open = df['Open]',
                    high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    volume = df['Volume'],
                    timeperiod = timeperiod)
        df[pattern] = npa_result.tolist()
        return df

    def AROON(self, df, timeperiod=-2**31):
        '''
        Aroon
        '''
        npa_result = talib.ADX(open = df['Open]',
                    high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    volume = df['Volume'],
                    timeperiod = timeperiod)
        df[pattern] = npa_result.tolist()
        return df

    def AROONOSC(self, df, timeperiod=-2**31):
        '''
        Aroon Oscillator
        '''
        npa_result = talib.ADX(open = df['Open]',
                    high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    volume = df['Volume'],
                    timeperiod = timeperiod)
        df[pattern] = npa_result.tolist()
        return df

    def BOP(self, df):
        '''
        Balance Of Power
        '''
        npa_result = talib.ADX(open = df['Open]',
                    high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    volume = df['Volume'],
                    timeperiod = timeperiod)
        df[pattern] = npa_result.tolist()
        return df

    def CCI(self, df):
        '''
        Commodity Channel Index
        '''
        npa_result = talib.ADX(open = df['Open]',
                    high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    volume = df['Volume'],
                    timeperiod = timeperiod)
        df[pattern] = npa_result.tolist()
        return df

    def CMO(self, df):
        '''
        Chande Momentum Oscillator
        '''
        npa_result = talib.ADX(open = df['Open]',
                    high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    volume = df['Volume'],
                    timeperiod = timeperiod)
        df[pattern] = npa_result.tolist()
        return df

    def DX(self, df):
        '''
        Directional Movement Index
        '''
        npa_result = talib.ADX(open = df['Open]',
                    high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    volume = df['Volume'],
                    timeperiod = timeperiod)
        df[pattern] = npa_result.tolist()
        return df

    def MACD(self, df):
        '''
        Moving Average Convergence/Divergence
        '''
        npa_result = talib.ADX(open = df['Open]',
                    high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    volume = df['Volume'],
                    timeperiod = timeperiod)
        df[pattern] = npa_result.tolist()
        return df

    def MACDEXT(self, df):
        '''
        MACD with controllable MA type
        '''
        npa_result = talib.ADX(open = df['Open]',
                    high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    volume = df['Volume'],
                    timeperiod = timeperiod)
        df[pattern] = npa_result.tolist()
        return df

    def MACDFIX(self, df):
        '''
        Moving Average Convergence/Divergence Fix 12/26
        '''
        npa_result = talib.ADX(open = df['Open]',
                    high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    volume = df['Volume'],
                    timeperiod = timeperiod)
        df[pattern] = npa_result.tolist()
        return df

    def MFI(self, df):
        '''
        Money Flow Index
        '''
        npa_result = talib.ADX(open = df['Open]',
                    high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    volume = df['Volume'],
                    timeperiod = timeperiod)
        df[pattern] = npa_result.tolist()
        return df

    def MINUS_DI(self, df):
        '''
        Minus Directional Indicator
        '''
        npa_result = talib.ADX(open = df['Open]',
                    high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    volume = df['Volume'],
                    timeperiod = timeperiod)
        df[pattern] = npa_result.tolist()
        return df

    def MINUS_DM(self, df):
        '''
        Minus Directional Movement
        '''
        npa_result = talib.ADX(open = df['Open]',
                    high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    volume = df['Volume'],
                    timeperiod = timeperiod)
        df[pattern] = npa_result.tolist()
        return df

    def MOM(self, df):
        '''
        Momentum
        '''
        npa_result = talib.ADX(open = df['Open]',
                    high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    volume = df['Volume'],
                    timeperiod = timeperiod)
        df[pattern] = npa_result.tolist()
        return df

    def PLUS_DI(self, df):
        '''
        Plus Directional Indicator
        '''
        npa_result = talib.ADX(open = df['Open]',
                    high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    volume = df['Volume'],
                    timeperiod = timeperiod)
        df[pattern] = npa_result.tolist()
        return df

    def PLUS_DM(self, df):
        '''
        Plus Directional Movement
        '''
        npa_result = talib.ADX(open = df['Open]',
                    high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    volume = df['Volume'],
                    timeperiod = timeperiod)
        df[pattern] = npa_result.tolist()
        return df

    def PPO(self, df):
        '''
        Percentage Price Oscillator
        '''
        npa_result = talib.ADX(open = df['Open]',
                    high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    volume = df['Volume'],
                    timeperiod = timeperiod)
        df[pattern] = npa_result.tolist()
        return df

    def ROC(self, df):
        '''
        Rate of change : ((price/prevPrice)-1)*100
        '''
        npa_result = talib.ADX(open = df['Open]',
                    high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    volume = df['Volume'],
                    timeperiod = timeperiod)
        df[pattern] = npa_result.tolist()
        return df

    def ROCP(self, df):
        '''
        Rate of change Percentage: (price-prevPrice)/prevPrice
        '''
        npa_result = talib.ADX(open = df['Open]',
                    high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    volume = df['Volume'],
                    timeperiod = timeperiod)
        df[pattern] = npa_result.tolist()
        return df

    def ROCR(self, df):
        '''
        Rate of change ratio: (price/prevPrice)
        '''
        npa_result = talib.ADX(open = df['Open]',
                    high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    volume = df['Volume'],
                    timeperiod = timeperiod)
        df[pattern] = npa_result.tolist()
        return df

    def ROCR100(self, df):
        '''
        Rate of change ratio 100 scale: (price/prevPrice)*100
        '''
        npa_result = talib.ADX(open = df['Open]',
                    high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    volume = df['Volume'],
                    timeperiod = timeperiod)
        df[pattern] = npa_result.tolist()
        return df

    def RSI(self, df):
        '''
        Relative Strength Index
        '''
        npa_result = talib.ADX(open = df['Open]',
                    high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    volume = df['Volume'],
                    timeperiod = timeperiod)
        df[pattern] = npa_result.tolist()
        return df

    def STOCH(self, df):
        '''
        Stochastic
        '''
        npa_result = talib.ADX(open = df['Open]',
                    high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    volume = df['Volume'],
                    timeperiod = timeperiod)
        df[pattern] = npa_result.tolist()
        return df

    def STOCHF(self, df):
        '''
        Stochastic Fast
        '''
        npa_result = talib.ADX(open = df['Open]',
                    high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    volume = df['Volume'],
                    timeperiod = timeperiod)
        df[pattern] = npa_result.tolist()
        return df

    def STOCHRSI(self, df):
        '''
        Stochastic Relative Strength Index
        '''
        npa_result = talib.ADX(open = df['Open]',
                    high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    volume = df['Volume'],
                    timeperiod = timeperiod)
        df[pattern] = npa_result.tolist()
        return df

    def TRIX(self, df):
        '''
        1-day Rate-Of-Change (ROC) of a Triple Smooth EMA
        '''
        npa_result = talib.ADX(open = df['Open]',
                    high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    volume = df['Volume'],
                    timeperiod = timeperiod)
        df[pattern] = npa_result.tolist()
        return df

    def ULTOSC(self, df):
        '''
        Ultimate Oscillator
        '''
        npa_result = talib.ADX(open = df['Open]',
                    high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    volume = df['Volume'],
                    timeperiod = timeperiod)
        df[pattern] = npa_result.tolist()
        return df

    def WILLR(self, df):
        '''
        Williams' %R
        '''
        npa_result = talib.ADX(open = df['Open]',
                    high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    volume = df['Volume'],
                    timeperiod = timeperiod)
        df[pattern] = npa_result.tolist()
        return df

#Done
class Volume(CategoryTemplate):
    '''
    Volume based indicators reside here

    Done
    '''
    def AD(self, df):
        '''
        Chaikin A/D Line

        Inputs:
            prices: ['high', 'low', 'close', 'volume']
        '''
        npa_result = talib.ADX(high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    volume = df['Volume'])
        df['AD'] = npa_result.tolist()
        return df

    def ADOSC(self, df, fastperiod=3, slowperiod=10):
        '''
        Chaikin A/D Oscillator

        Inputs:
            prices: ['high', 'low', 'close', 'volume']
        Parameters:
            fastperiod: 3
            slowperiod: 10
        '''
        npa_result = talib.ADX(high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    volume = df['Volume'],
                    fastperiod = fastperiod,
                    slowperiod = slowperiod)
        df['ADOSC ' + str(fastperiod) + ' ' + str(slowperiod)] = npa_result.tolist()
        return df

    def OBV(self, df, key='Close'):
        '''
        On Balance Volume

        Inputs:
            real: (any ndarray)
            prices: ['volume']
        '''
        npa_result = talib.ADX(real = df[real],
                    volume = df['Volume'])
        df['OBV ' + key] = npa_result.tolist()
        return df

#Done
class Volatility(CategoryTemplate):
    '''
    Volatility based indicators reside here
    '''
    def ATR(self, df, timeperiod=14):
        '''
        Average True Range

        Inputs:
            prices: ['high', 'low', 'close']
        Parameters:
            timeperiod: 14
        '''
        npa_result = talib.ATR(high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    timeperiod = timeperiod)
        df['ATR ' + str(timeperiod)] = npa_result.tolist()
        return df

    def NATR(self, df, timeperiod=14):
        '''
        Normalized Average True Range

        Inputs:
            prices: ['high', 'low', 'close']
        Parameters:
            timeperiod: 14
        '''
        npa_result = talib.ATR(high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    timeperiod = timeperiod)
        df['NATR ' + str(timeperiod)] = npa_result.tolist()
        return df

    def TRANGE(self, df):
        '''
        True Range

        Inputs:
            prices: ['high', 'low', 'close']
        '''
        npa_result = talib.ATR(high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    timeperiod = timeperiod)
        df['TRANGE'] = npa_result.tolist()
        return df

#TODO
class Cycle(CategoryTemplate):
    '''
    Cycle based indicators reside here
    '''
    def HT_DCPERIOD(self, df, key='Close'):
        '''
        Hilbert Transform - Dominant Cycle Period

        Inputs:
            real: (any ndarray)
        '''
        npa_result = talib.HT_DCPERIOD(high = df[key])
        df['HT_DCPERIOD'] = npa_result.tolist()
        return df
    def HT_DCPHASE(self, df):
        '''
        Hilbert Transform - Dominant Cycle Phase
        '''
    def HT_PHASOR(self, df):
        '''
        Hilbert Transform - Phasor Components
        '''
    def HT_SINE(self, df):
        '''
        Hilbert Transform - SineWave
        '''
    def HT_TRENDMODE(self, df):
        '''
        Hilbert Transform - Trend vs Cycle Mode
        '''

#Mostly done
class Indicator:
    '''
    A class to precompute loads of indicators
    Also serves as a container to keep things organized
    '''
    def __init__(self, tapandascompat):
        self.momentum = Momentum(tapandascompat)
        self.volume = Volume(tapandascompat)
        self.volatility = Volatility(tapandascompat)
        self.cycle = Cycle(tapandascompat)
    def precompute(self):
        pass

#TODO
class Overlap(CategoryTemplate):
    '''
    A class to precompute loads of overlap sets
    '''
    def __init__(self, tapandascompat):
        super().__init__(tapandascompat)
    def precompute(self):
        pass

    def BBANDS(self, df):
        '''
        Bollinger Bands
        '''
    def DEMA(self, df):
        '''
        Double Exponential Moving Average
        '''
    def EMA(self, df):
        '''
        Exponential Moving Average
        '''
    def HT_TRENDLINE(self, df):
        '''
        Hilbert Transform - Instantaneous Trendline
        '''
    def KAMA(self, df):
        '''
        Kaufman Adaptive Moving Average
        '''
    def MA(self, df):
        '''
        Moving average
        '''
    def MAMA(self, df):
        '''
        MESA Adaptive Moving Average
        '''
    def MAVP(self, df):
        '''
        Moving average with variable period
        '''
    def MIDPOINT(self, df):
        '''
        MidPoint over period
        '''
    def MIDPRICE(self, df):
        '''
        Midpoint Price over period
        '''
    def SAR(self, df):
        '''
        Parabolic SAR
        '''
    def SAREXT(self, df):
        '''
        Parabolic SAR - Extended
        '''
    def SMA(self, df):
        '''
        Simple Moving Average
        '''
    def T3(self, df):
        '''
        Triple Exponential Moving Average (T3)
        '''
    def TEMA(self, df):
        '''
        Triple Exponential Moving Average
        '''
    def TRIMA(self, df):
        '''
        Triangular Moving Average
        '''
    def WMA(self, df):
        '''
        Weighted Moving Average
        '''

#Done
class Candlestick(CategoryTemplate):
    '''
    Wrapper for the candlestick recognition functionalities in TA-Lib.

    Remember that, while the TALib documentation says that the candlestick
    pattern searches return either 100 or -100, they also return 0.

    From what I can tell, 100 is match (for sure), -100 indicates a partial
    match of the pattern but the pattern failing to complete, and 0 indicates
    that the pattern never started.
    '''
    def __init__(self, tapandascompat):
        super().__init__(tapandascompat)
        self.func_dict = {}
        for item in dir(talib):
            if item[0:3] == 'CDL':
                self.func_dict[item] = eval('talib.'+item)

    def compute_candle(self, pattern, df):
        '''
        Compute instances of a given candle given a dataframe

        Takes arguments pattern and df.
        Pattern is a string name for the candle.  Use get_list_candles() to
            find supported candlestick names.
        df is a pandas Dataframe.
        '''
        npa_result = self.func_dict[pattern](open = df['Open'].values,
                      high = df['High'].values,
                      low = df['Low'].values,
                      close = df['Close'].values)
        df[pattern] = npa_result.tolist()
        resp = df[pattern]
        return resp

    def precompute(self, df, width=1):
        for candle in self.func_dict.keys():
            resp = self.compute_candle(candle, df)
            #Put in the width parameter in case I want to go to two day/unit candle width
            self.compat.abstractions.write_csv_sym(resp, csv_type=candle + '_' + str(width))

    def get_list_candles(self):
        return self.func_dict.keys()

#Mostly done
class PandasTALib:
    '''
    A class to hold abstractions to make TALib calls easier.

    Currently one argument to __init__ is abstractions.

    The argument abstractions needs to be a class that contains several methods
    to function properly.  They are currently:

    write_csv_sym
    read_csv_sym

    Even if these are not present, the wrapper will still function as a way to
    make calls with pandas series.  The full pre-compute functionality will not,
    however, be available.

    The things that you can get directly from pandas which are also in ta-lib
    aren't wrapped here at all, think rolling avg etc.
    '''
    def __init__(self, abstractions):
        self.candle = Candlestick(self)
        self.indicator = Indicator(self)
        self.overlap = Overlap(self)
        self.abstractions = abstractions


    def precompute(self):
        self.candle.precompute()
        self.indicator.precompute()
        self.overlap.precompute()

if __name__ == '__main__':
    pass
