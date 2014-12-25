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

#TODO
#Add default values to each call
#Put in the df splitting logic
#Put in the df joining logic
#Add a brief explanation of each indicator/other to the docstring for the
#   indicator/other.  Think, the about/explanation from chartschool.com.
#Add examples to example.py
#Add "fields" to "retvals" so it's easier to be programtically indiscriminate
#   to each function.
#   Due to the goal of this particular wrapper, this may mean adding non-talib functions
#       such that you could turn "multiple return value crossover" or similar in to a
#       separate binary indicator.

#Done
class CategoryTemplate:
    def __init__(self, tapandascompat):
        self.compat = tapandascompat

#Mostly done
class Momentum(CategoryTemplate):
    '''
    All momentum indicators reside here.
    '''
    #Ignore - works fine.
    def __init__(self, tapandascompat):
        super().__init__(tapandascompat)

    def ADX(self, df, timeperiod=14):
        '''
        Average Directional Movement Index
        '''
        npa_result = talib.ADX(high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    timeperiod = timeperiod)
        df['ADX'] = npa_result.tolist()
        return df

    def ADXR(self, df, timeperiod=14):
        '''
        Average Directional Movement Index Rating
        '''
        npa_result = talib.ADXR(high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    timeperiod = timeperiod)
        df['ADXR'] = npa_result.tolist()
        return df

    def APO(self, df, key='close', fastperiod=14 , slowperiod=14 , matype=0):
        '''
        Absolute Price Oscillator
        '''
        npa_result = talib.APO(df[key],
                    fastperiod = fastperiod,
                    slowperiod = slowperiod,
                    matype = matype)
        df['APO'] = npa_result.tolist()
        return df

    def AROON(self, df, timeperiod=14):
        '''
        Aroon

        #TODO retvals
        Outputs:
        aroondown
        aroonup
        '''
        npa_result = talib.AROON(high = df['High'],
                    low = df['Low'],
                    timeperiod = timeperiod)
        df['AROON'] = npa_result.tolist()
        return df

    def AROONOSC(self, df, timeperiod=14):
        '''
        Aroon Oscillator
        '''
        npa_result = talib.AROONOSC(high = df['High'],
                    low = df['Low'],
                    timeperiod = timeperiod)
        df['AROONOSC'] = npa_result.tolist()
        return df

    def BOP(self, df, timeperiod=14):
        '''
        Balance Of Power
        '''
        npa_result = talib.BOP(open = df['Open'],
                    high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    timeperiod = timeperiod)
        df['BOP'] = npa_result.tolist()
        return df

    def CCI(self, df, timeperiod=14):
        '''
        Commodity Channel Index
        '''
        npa_result = talib.CCI(high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    timeperiod = timeperiod)
        df['CCI'] = npa_result.tolist()
        return df

    def CMO(self, df, key='Close', timeperiod=14):
        '''
        Chande Momentum Oscillator
        '''
        npa_result = talib.CMO(close = df['Close'],
                    timeperiod = timeperiod)
        df['CMO'] = npa_result.tolist()
        return df

    def DX(self, df, timeperiod=14):
        '''
        Directional Movement Index
        '''
        npa_result = talib.DX(high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    timeperiod = timeperiod)
        df['DX'] = npa_result.tolist()
        return df

    def MACD(self, df, key="Close", fastperiod=12, slowperiod=26, signalperiod=9):
        '''
        Moving Average Convergence/Divergence

        #TODO - the retvals
        macd
        macdsignal
        macdhist        
        '''
        npa_result = talib.MACD(df[key],
                    fastperiod = fastperiod,
                    slowperiod = slowperiod,
                    signalperiod = signalperiod)
        df['MACD'] = npa_result.tolist()
        return df

    def MACDEXT(self, df, key='Close',
                fastperiod=12,
                fastmatype=0,
                slowperiod=26,
                slowmatype=0,
                signalperiod=9,
                signalmatype=0):
        '''
        MACD with controllable MA type

        #TODO - the retvals
        Outputs:
            macd
            macdsignal
            macdhist
        '''
        npa_result = talib.MACDEXT(df[key],
                fastperiod=12,
                fastmatype=0,
                slowperiod=26,
                slowmatype=0,
                signalperiod=9,
                signalmatype=0)
        df['MACDEXT'] = npa_result.tolist()
        return df

    def MACDFIX(self, df, key='Close', signalperiod=9):
        '''
        Moving Average Convergence/Divergence Fix 12/26

        #TODO
        Outputs:
            macd
            macdsignal
            macdhist
        '''
        npa_result = talib.MACDFIX(open = df[key],
                    signalperiod = signalperiod)
        df['MACDFIX'] = npa_result.tolist()
        return df

    def MFI(self, df, timeperiod=14):
        '''
        Money Flow Index
        '''
        npa_result = talib.MFI(high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    volume = df['Volume'],
                    timeperiod = timeperiod)
        df['MFI'] = npa_result.tolist()
        return df

    def MINUS_DI(self, df, timeperiod=14):
        '''
        Minus Directional Indicator
        '''
        npa_result = talib.MINUS_DI(high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    timeperiod = timeperiod)
        df['MINUS_DI'] = npa_result.tolist()
        return df

    def MINUS_DM(self, df, timeperiod=14):
        '''
        Minus Directional Movement
        '''
        npa_result = talib.MINUS_DM(high = df['High'],
                    low = df['Low'],
                    timeperiod = timeperiod)
        df['MINUS_DM'] = npa_result.tolist()
        return df

    def MOM(self, df, key='Close', timeperiod=10):
        '''
        Momentum

        #TODO check all key= for appropriate keys...
        I don't know all these.
        '''
        npa_result = talib.MOM(open = df[key],
                    timeperiod = timeperiod)
        df['MOM'] = npa_result.tolist()
        return df

    def PLUS_DI(self, df, timeperiod=14):
        '''
        Plus Directional Indicator
        '''
        npa_result = talib.PLUS_DI(high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    timeperiod = timeperiod)
        df['PLUS_DI'] = npa_result.tolist()
        return df

    def PLUS_DM(self, df, timeperiod=14):
        '''
        Plus Directional Movement
        '''
        npa_result = talib.PLUS_DM(high = df['High'],
                    low = df['Low'],
                    timeperiod = timeperiod)
        df['PLUS_DM'] = npa_result.tolist()
        return df

    def PPO(self, df, key='Close',
        fastperiod=12,
        slowperiod=26,
        matype=0):
        '''
        Percentage Price Oscillator
        '''
        npa_result = talib.PPO(open = df['Open'],
                    high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    volume = df['Volume'],
                    timeperiod = timeperiod)
        df['PPO'] = npa_result.tolist()
        return df

    def ROC(self, df, key='Close', timeperiod=10):
        '''
        Rate of change : ((price/prevPrice)-1)*100
        '''
        npa_result = talib.ROC(close = df['Close'],
                    timeperiod = timeperiod)
        df['ROC'] = npa_result.tolist()
        return df

    def ROCP(self, df, key='Close', timeperiod=10):
        '''
        Rate of change Percentage: (price-prevPrice)/prevPrice
        '''
        npa_result = talib.ROCP(close = df['Close'],
                    timeperiod = timeperiod)
        df['ROCP'] = npa_result.tolist()
        return df

    def ROCR(self, df, key='Close', timeperiod=10):
        '''
        Rate of change ratio: (price/prevPrice)
        '''
        npa_result = talib.ROCR(open = df[key],
                    timeperiod = timeperiod)
        df['ROCR'] = npa_result.tolist()
        return df

    def ROCR100(self, df, key='Close', timeperiod=10):
        '''
        Rate of change ratio 100 scale: (price/prevPrice)*100
        '''
        npa_result = talib.ROCR100(open = df[key],
                    timeperiod = timeperiod)
        df['ROCR100'] = npa_result.tolist()
        return df

    def RSI(self, df, key='Close', timeperiod=14):
        '''
        Relative Strength Index
        '''
        npa_result = talib.RSI(open = df[key],
                    timeperiod = timeperiod)
        df['RSI'] = npa_result.tolist()
        return df

    def STOCH(self,
            df,
            fastk_period=5,
            slowk_period=3,
            slowk_matype=0,
            slowd_period=3,
            slowd_matype=0):
        '''
        Stochastic

        #TODO retvals
        '''
        npa_result = talib.STOCH(high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    fastk_period=fastk_period,
                    slowk_period=slowk_period,
                    slowk_matype=slowk_matype,
                    slowd_period=slowd_period,
                    slowd_matype=slowd_matype)
        df['STOCH'] = npa_result.tolist()
        return df

    def STOCHF(self,
            df
            fastk_period=5,
            fastd_period=3,
            fastd_matype=0):
        '''
        Stochastic Fast

        #TODO retvals
        '''
        npa_result = talib.STOCHF(open = df['Open'],
                    high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    volume = df['Volume'],
                    timeperiod = timeperiod)
        df['STOCHF'] = npa_result.tolist()
        return df

    def STOCHRSI(self,
            df,
            key='Close',
            timeperiod=14,
            fastk_period=5,
            fastd_period=3,
            fastd_matype=0):
        '''
        Stochastic Relative Strength Index

        #TODO retvals
        '''
        npa_result = talib.STOCHRSI(df[key],
            timeperiod=timeperiod,
            fastk_period=fastk_period,
            fastd_period=fastd_period,
            fastd_matype=fastd_matype)
        df['STOCHRSI'] = npa_result.tolist()
        return df

    def TRIX(self, df, key='Close', timeperiod=30):
        '''
        1-day Rate-Of-Change (ROC) of a Triple Smooth EMA
        '''
        npa_result = talib.TRIX(df[key],
                    timeperiod = timeperiod)
        df['TRIX'] = npa_result.tolist()
        return df

    def ULTOSC(self,
        df,
        timeperiod1=7,
        timeperiod2=14,
        timeperiod3=28):
        '''
        Ultimate Oscillator
        '''
        npa_result = talib.ULTOSC(high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    timeperiod1=7,
                    timeperiod2=14,
                    timeperiod3=28)
        df['ULTOSC'] = npa_result.tolist()
        return df

    def WILLR(self, df, timeperiod=14):
        '''
        Williams' %R
        '''
        npa_result = talib.WILLR(high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
                    timeperiod = timeperiod)
        df['WILLR'] = npa_result.tolist()
        return df

#Mostly done
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
        '''
        npa_result = talib.ADX(df[key],
                    volume = df['Volume'])
        df['OBV ' + key] = npa_result.tolist()
        return df

#Mostly done
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

#Mostly done
class Cycle(CategoryTemplate):
    '''
    Cycle based indicators reside here
    '''
    def HT_DCPERIOD(self, df, key='Close'):
        '''
        Hilbert Transform - Dominant Cycle Period
        '''
        npa_result = talib.HT_DCPERIOD(df[key])
        df['HT_DCPERIOD'] = npa_result.tolist()
        return df
    def HT_DCPHASE(self, df, key='Close'):
        '''
        Hilbert Transform - Dominant Cycle Phase
        '''
        npa_result = talib.HT_DCPHASE(df[key])
        df['HT_DCPHASE'] = npa_result.tolist()
        return df
    def HT_PHASOR(self, df, key='Close'):
        '''
        Hilbert Transform - Phasor Components
        Outputs:
            inphase
            quadrature
        #TODO
        '''
        npa_result = talib.HT_PHASOR(df[key])
        df['HT_PHASOR'] = npa_result.tolist()
        return df
    def HT_SINE(self, df, key='Close'):
        '''
        Hilbert Transform - SineWave
        Outputs:
            sine
            leadsine        
        #TODO
        '''
        npa_result = talib.HT_DCPERIOD(df[key])
        df['HT_SINE'] = npa_result.tolist()
        return df
    def HT_TRENDMODE(self, df, key='Close'):
        '''
        Hilbert Transform - Trend vs Cycle Mode
        Outputs:
            integer (values are -100, 0 or 100)
        '''
        npa_result = talib.HT_DCPERIOD(df[key])
        df['HT_TRENDMODE'] = npa_result.tolist()
        return df

#Done
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
        self.momentum.precompute()
        self.volume.precompute()
        self.volatility.precompute()
        self.cycle.precompute()

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

        #TODO
        Outputs:
            upperband
            middleband
            lowerband
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
