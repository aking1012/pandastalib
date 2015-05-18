#!/usr/bin/env python3

import pandas, os, datetime, csv

from .stockDbSync import db, StockTick

#Convenience classes for analysis and testing
class Abstractions:
    '''
    A class to hold useful abstractions for things that
    I'll reuse over and over.
    '''
    def __init__(self, manage_tickers):
        '''
        '''
        home = os.path.expanduser("~")
        self.app_stores = os.path.join(home, '.local', 'share', 'stockdb')

        self.ticker = ''
        self.exchange = ''
        self.tickers = manage_tickers
        self.ta = ''
        self.df = ''
        self.db = db

    def update_tickers(self):
        #TODO this is now broken, update it a little to unbreak it for performance
        #benchmark/comparison on multiprocess to non-multiprocess and other
        #enhancements.
        self.tickers.update()

    def precompute(self,
                    exchange_target=False,
                    ticker_target=False,
                    category=False):
        '''
        TODO move the iteritems thing in to a routine... but that's for later.
        I need desperately to make this work.
        '''
        for exchange in self.tickers.exchanges.exchanges_list():
            if (exchange_target and exchange[0]==exchange_target) or not exchange_target:
                for ticker in self.tickers.exchanges.tickers(exchange):
                    if (ticker_target and ticker==ticker_target) or not ticker_target:
                        self.ta.precompute(ticker, category=category)

    def precompute_other(self, exchange_target=False, ticker_target=False, category=False):
        for exchange in self.tickers.exchanges.exchanges_list():
            if (exchange_target and exchange[0]==exchange_target) or not exchange_target:
                for ticker in self.tickers.exchanges.tickers(exchange):
                    if (ticker_target and ticker==ticker_target) or not ticker_target:
                        #Make this work for non-standard precomputes.
                        #Think - convert things to percentages
                        #Rolling averages etc...
                        pass

    def exchange_from_ticker(self):
        '''
        ta.abstractions.exchange_from_ticker() 'FLWS' should yield NASDAQ
        ta.abstractions.exchange_from_ticker() 'DDD' should yield NYSE
        ta.abstractions.exchange_from_ticker() 'XXII' should yield AMEX
        '''
        files = []
        for (dirpath, dirnames, filenames) in os.walk(self.app_stores):
            files.extend(filenames)
            break
        for exchange_name in files:
            with open(os.path.join(self.app_stores, exchange_name), 'r') as exchange_csv:
                exchange = csv.DictReader(exchange_csv)
                for sym in exchange:
                    if sym['Symbol'] == self.ticker:
                        self.exchange = exchange_name.split('.csv')[0]
                        return

    def read_csv_sym(self, csv_type=False):
        try:
            fname = os.path.join(self.app_stores, self.exchange, self.ticker, csv_type + '.csv')
            return pandas.io.parsers.read_table(fname, index_col=0, sep=',', quotechar='"', header='infer', low_memory=True, parse_dates=True, infer_datetime_format=True)
        except:
            return False

    def write_csv_sym(self, csv_type=False):
        if not csv_type: return
        with open(os.path.join(self.app_stores, self.exchange, self.ticker, csv_type + '.csv'), 'w') as fname:
            self.df.to_csv(fname)

    def date_slice(self, start, end):
        '''
        I'll need this for when I parse lookback using the abstract talib api
        and try to do incremental updates.
        '''
        start = start.split('-')
        end = end.split('-')
        start = self.df.index.searchsorted(datetime.datetime(int(start[0]), int(start[1]), int(start[2])))
        end = self.df.index.searchsorted(datetime.datetime(int(end[0]), int(end[1]), int(end[2])))
        self.df = self.df.ix[start:end]

    def load_all_precomputes_csv(self):
        self.clean_csv()
        self.df = pandas.DataFrame()
        for item in self.ta.ta_funcs:
            temp_df = self.read_csv_sym(csv_type=item)
            if not type(temp_df) == bool:
                self.df = pandas.concat([self.df, temp_df], axis=1)
        self.df['TICKER'] = pandas.Series(self.ticker, index=self.df.index)
        self.clean_df()

    def clean_df(self):
        '''
        Make all upper case
        Remove duplicate columns
        #Log duplicate columns, so eventually we just remove them
        '''
        self.df.columns = [x.upper() for x in self.df.columns]
        self.df = self.df.T.groupby(level=0).first().T

    def clean_csv(self):
        ticker = self.ticker
        exchange = self.exchange_from_ticker()
        for csv_type in self.ta.ta_funcs:
            fname = os.path.join(self.app_stores, self.exchange, self.ticker, csv_type + '.csv')
            try:
                tmp = ''
                with open(fname, 'r') as r:
                    tmp = r.readline()
                if "Date" not in tmp:
                    with open(fname, 'r+') as f:
                        line = 'Date,' + csv_type + '\n'
                        content = f.read()
                        f.seek(0, 0)
                        f.write(line + content)
            except:
                pass

    def clean_all_csvs(self):
        for exchange in self.tickers.exchanges.exchanges_list():
            for ticker in self.tickers.exchanges.tickers(exchange):
                self.ticker = ticker
                self.clean_csv()

    def save_df_sql(self):
        for index, row in self.df.iterrows():
            temp = StockTick(index, row)
            self.db.session.add(temp)
        self.db.session.commit()

    def save_all_precomputes_sql(self):
        #TODO add logging and timers
        for exchange, ticker in self.tickers:
            print(exchange, ticker)
            self.ticker = ticker
            self.read_csv_sym()
            try:
                self.clean_csv()
            except:
                pass
            self.load_all_precomputes_csv()
            self.clean_df()
            self.save_df_sql()
