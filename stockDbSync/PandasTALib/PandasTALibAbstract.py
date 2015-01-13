import datetime, code, os, talib, pandas, csv
from talib import abstract
import numpy

#Still have to inspect and group for the organized abstract API

class PandasFunction(abstract.Function):
    def __init__(self, function_name):
        '''
        Most basic test:

        CDLDOJI = PandasFunction('CDLDOJI')
        #Have to figure out why I have to do this twice...
        CDLDOJI.set_input_arrays(df)
        CDLDOJI.set_input_arrays(df)
        CDLDOJI()
        '''
        super().__init__(function_name)

    def set_input_arrays(self, input_data):
        '''
        For whatever reason, I have to run this twice...
        Bug I need to troubleshoot a bit.
        '''
        try:
            super().set_input_arrays(input_data)
            return True
        except:
            pass
        column_names = []
        try:
            i=0
            while(True):
                column_names.append(input_data.columns[i])
                i+=1
        except IndexError as e:
            e = e
        names_lower = [item.lower() for item in column_names]
        name_dict = {}
        i=0
        for item in column_names:
            name_dict[item] = names_lower[i]
            i+=1
        input_data.rename(columns=name_dict, inplace=True)
        temp = input_data['volume'].values.astype('double')
        input_data['volume'] = temp
        super().set_input_arrays(input_data[names_lower].values)
        return True

class CategoryTemplate:
    def __init__(self, tapandascompat):
        self.compat = tapandascompat

class Momentum(CategoryTemplate):
    '''
    All momentum indicators reside here.
    '''
    #Ignore - works fine.
    def __init__(self, tapandascompat):
        super().__init__(tapandascompat)

    def precompute(self, ticker, exchange=False, csv_type=False):
        return

class Volume(CategoryTemplate):
    '''
    Volume based indicators reside here

    Done
    '''
    def __init__(self, tapandascompat):
        super().__init__(tapandascompat)

    def precompute(self, ticker, exchange=False, csv_type=False):
        pass

class Volatility(CategoryTemplate):
    '''
    Volatility based indicators reside here
    '''
    def __init__(self, tapandascompat):
        super().__init__(tapandascompat)

    def precompute(self, ticker, exchange=False, csv_type=False):
        pass

class Cycles(CategoryTemplate):
    '''
    Cycle based indicators reside here
    '''
    def __init__(self, tapandascompat):
        super().__init__(tapandascompat)

    def precompute(self, ticker, exchange=False, csv_type=False):
        pass

class Indicators:
    '''
    A class to precompute loads of indicators
    Also serves as a container to keep things organized
    '''
    def __init__(self, tapandascompat):
        self.momentum = Momentum(tapandascompat)
        self.volume = Volume(tapandascompat)
        self.volatility = Volatility(tapandascompat)
        self.cycles = Cycles(tapandascompat)

    def precompute(self, ticker, exchange=False, csv_type=False):
        self.momentum.precompute(ticker, exchange=False, csv_type=False)
        self.volume.precompute(ticker, exchange=False, csv_type=False)
        self.volatility.precompute(ticker, exchange=False, csv_type=False)
        self.cycles.precompute(ticker, exchange=False, csv_type=False)

class Overlaps(CategoryTemplate):
    '''
    A class to precompute loads of overlap sets
    '''
    def __init__(self, tapandascompat):
        super().__init__(tapandascompat)

    def precompute(self, ticker, exchange=False, csv_type=False):
        pass

class Candlesticks(CategoryTemplate):
    '''
    Wrapper for the candlestick recognition functionalities in TA-Lib.

    Remember that, while the TALib documentation says that the candlestick
    pattern searches return either 100 or -100, they also return 0.
    '''
    def __init__(self, tapandascompat):
        super().__init__(tapandascompat)

class PandasTALib:
    '''
    A class to hold abstractions to make TALib calls easier.

    Currently one argument to __init__ is abstractions.

    The argument abstractions needs to be a class that contains several methods
    to function properly.  They are currently:

    write_csv_sym
    read_csv_sym
    exchange_from_ticker
    update_tickers

    I provide a basic abstractions class for use if you want it.  It's not how I
    personally use it, but it's there for portability and testing.

    #TODO add functions in their respective places from here...
    '''
    def __init__(self, abstractions, ta_funcs):
        self.candles = Candlesticks(self)
        self.indicators = Indicators(self)
        self.overlaps = Overlaps(self)
        self.abstractions = abstractions
        self.ta_funcs = ta_funcs

    def precompute(self, ticker, exchange=False, category=False):
        #TODO add parameter tweaking here...  for now, just using defaults is
        #fine.

        #TODO add category computation, so you could have one box/process run
        #a portion of the calculations and another other bits.

        if not exchange: exchange = self.abstractions.exchange_from_ticker(ticker)
        data = self.abstractions.read_csv_sym(ticker, exchange)
        try:
            if not data: return
        except ValueError as e:
            #This catches the error for when data would normally pythonically be True.
            #However, dataframes don't like the if exists True operation/trick and
            #  throw a ValueError instead.
            e = e
        for item in self.ta_funcs:
            if item == 'MAVP':
                #We don't need to do multiple moving averages at once.
                #Added bonus, we don't have to probe for inputs.  A frame works
                #all across the board.

                #Set parameters would be nice though.
                continue
            temp_func = PandasFunction(item)
            #Need to figure out why it pukes if I don't call this twice...
            temp_func.set_input_arrays(data)
            temp_func.set_input_arrays(data)
            frame = temp_func()
            self.abstractions.write_csv_sym(frame, csv_type=item)

#TODO BEFORE YOU DELETE ME REMEMBER TO COPY ME BACK WHERE I BELONG...
#Convenience classes for analysis and testing
#Since everything isn't installed yet, some of this just holds a pass,
#  but when it's imported and constructed, they're live calls.
#Will be removed from this particular file once manual testing is complete.
#It's here now, so I can pick through functions and test them manually dropping
#  to a terminal
class Abstractions:
    '''
    A class to hold useful abstractions for things that I'll reuse over and over.
    '''
    def __init__(self):
        '''
        '''
        home = os.path.expanduser("~")
        self.app_stores = os.path.join(home, '.config', 'stockdb')

        self.ticker = ''
        self.exchange = ''

    def update_tickers(self):
        pass

    def exchange_from_ticker(self, ticker):
        '''
        ta.abstractions.exchange_from_ticker('FLWS') should yield NASDAQ
        ta.abstractions.exchange_from_ticker('DDD') should yield NYSE
        ta.abstractions.exchange_from_ticker('XXII') should yield AMEX
        '''
        files = []
        for (dirpath, dirnames, filenames) in os.walk(self.app_stores):
            files.extend(filenames)
            break
        for exchange_name in files:
            with open(os.path.join(self.app_stores, exchange_name), 'r') as exchange_csv:
                exchange = csv.DictReader(exchange_csv)
                for sym in exchange:
                    if sym['Symbol'] == ticker:
                        return exchange_name.split('.csv')[0]

    def read_csv_sym(self, ticker, exchange=False, csv_type=False):
        if not csv_type: csv_type = ticker
        self.ticker = ticker
        if not exchange: exchange = self.exchange_from_ticker(ticker)
        self.exchange = exchange
        fname = os.path.join(self.app_stores, exchange, ticker, csv_type + '.csv')
        return pandas.io.parsers.read_table(fname, index_col=0, sep=',', quotechar='"', header='infer', low_memory=True, parse_dates=True, infer_datetime_format=True)

    def write_csv_sym(self, df, csv_type=False):
        if not csv_type: return
        with open(os.path.join(self.app_stores, self.exchange, self.ticker, csv_type + '.csv'), 'w') as fname:
            df.to_csv(fname)

if __name__ == '__main__':
    ta = PandasTALib(Abstractions(), ta_funcs=abstract.__FUNCTION_NAMES)
    df = ta.abstractions.read_csv_sym('FLWS', 'NASDAQ')
    #ta.precompute('FLWS')
    code.interact(local = locals())
