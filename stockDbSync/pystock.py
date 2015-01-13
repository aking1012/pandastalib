#!/usr/bin/env python3

import pandas, os, datetime, talib, csv, code
import stockDbSync, PandasTALib, Analysis

#Many features are not yet implemented, but many are.  At least it precomputes
#properly now.  So, it's a start.

#Convenience classes for analysis and testing
class Abstractions:
    '''
    A class to hold useful abstractions for things that I'll reuse over and over.
    '''
    def __init__(self, manage_tickers):
        '''
        '''
        home = os.path.expanduser("~")
        self.app_stores = os.path.join(home, '.config', 'stockdb')

        self.ticker = ''
        self.exchange = ''
        self.tickers = manage_tickers
        self.ta = ''
        self.analysis = Analysis.analysis.Analysis(self)

    def update_tickers(self, exchange=False, ticker=False):
        self.tickers.update_tickers(exchange, ticker)

    def precompute(self, exchange_target=False, ticker_target=False, category=False):
        for exchange in self.tickers.exchanges.exchanges_list():
            if (exchange_target and exchange[0]==exchange_target) or not exchange_target:
                for ticker in self.tickers.exchanges.tickers(exchange):
                    if (ticker_target and ticker==ticker_target) or not ticker_target:
                        self.ta.precompute(ticker, category=category)



    def exchange_from_ticker(self, ticker):
        '''
        ta.abstractions.exchange_from_ticker('FLWS') should yield NASDAQ
        ta.abstractions.exchange_from_ticker('FLWS') should yield NYSE
        ta.abstractions.exchange_from_ticker('FLWS') should yield AMEX
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
        try:
            fname = os.path.join(self.app_stores, exchange, ticker, csv_type + '.csv')
            return pandas.io.parsers.read_table(fname, index_col=0, sep=',', quotechar='"', header='infer', low_memory=True, parse_dates=True, infer_datetime_format=True)
        except:
            return False

    def write_csv_sym(self, df, csv_type=False):
        if not csv_type: return
        with open(os.path.join(self.app_stores, self.exchange, self.ticker, csv_type + '.csv'), 'w') as fname:
            df.to_csv(fname)

    def date_slice(self, ticker_data, start, end):
        '''
        '''
        start = start.split('-')
        end = end.split('-')
        start = ticker_data.index.searchsorted(datetime.datetime(int(start[0]), int(start[1]), int(start[2])))
        end = ticker_data.index.searchsorted(datetime.datetime(int(end[0]), int(end[1]), int(end[2])))
        return ticker_data.ix[start:end]

    def set_ta(self, ta):
        self.ta = ta


if __name__ == '__main__':
    manage_tickers = stockDbSync.ManageTickers()
    abstract = Abstractions(manage_tickers)
    ta = PandasTALib.Abstract(abstract, talib.abstract.__FUNCTION_NAMES)
    abstract.set_ta(ta)
    code.interact(local = locals())
