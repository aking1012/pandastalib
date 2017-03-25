import pandas, os, datetime, csv

#Convenience classes for analysis and testing
class Abstractions:
    '''
    A class to hold useful abstractions for things that
    I'll reuse over and over.
    '''
    def __init__(self, manage_tickers):
        home = os.path.expanduser("~")
        self.app_stores = os.path.join(home, '.local', 'share', 'stockdb')

        self.ticker = ''
        self.exchange = ''
        self.tickers = manage_tickers
        self.ta = ''
        self.df = ''

    def multi_update_all(self):
        start = datetime.datetime.now()
        self.tickers.multi_update()
        self.ta.multi_precompute()
        i=0
        while not self.tickers.in_q.empty():
            i+=1
            self.ta.in_q.put(self.tickers.out_q.get(timeout=5))
            print(datetime.datetime.now() - start)
            print(str(i) + ' records fetched')
        print('Total run time for initial db sync:')
        print(datetime.datetime.now() - start)
        i=0
        while not (self.ta.in_q.empty() and self.ta.out_q.empty()):
            i+=1
            (exchange, ticker) = self.ta.out_q.get()
            print(datetime.datetime.now() - start)
            print(str(i) + ' precomputes completed')
            #Do additional process queue-ing
        print("All done...  Total time to fetch and compute:")
        print(datetime.datetime.now() - start)
        print("Now to speed up migration to the database...")
        print("And kill off all those child processes.....")

    def multi_update_one(self, exchange='NASDAQ', ticker='FLWS'):
        '''
        Used for debugging and feature testing
        '''
        start = datetime.datetime.now()
        self.tickers.multi_update(exchange=exchange, ticker=ticker)
        self.ta.multi_precompute()
        self.ta.in_q.put(self.tickers.out_q.get(timeout=5))
        print(datetime.datetime.now() - start)
        print('1 records fetched')
        print(datetime.datetime.now() - start)
        (exchange, ticker) = self.ta.out_q.get()
        print(datetime.datetime.now() - start)
        print('1 precomputes completed')


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

    def read_csv_sym(self, csv_type=False, ticker=False):
        print("Trying: " + self.ticker + ' ' + csv_type)
        self.exchange_from_ticker()
        try:
            fname = os.path.join(self.app_stores, self.exchange, self.ticker, csv_type + '.csv')
            return pandas.io.parsers.read_csv(fname, index_col=0, header='infer', low_memory=True, parse_dates=True, infer_datetime_format=True)
        except OSError:
            print('failed to read csv for ' + self.ticker)
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

    def prep_db_migration(self):
        self.df['TICKER'] = pandas.Series(self.ticker, index=self.df.index)
        self.df['EXCHANGE'] = pandas.Series(self.exchange, index=self.df.index)

    def load_all_precomputes_csv(self):
        #TODO just iter over CSVs instead of tafuncs, so it just works with new precomputes
        self.clean_csv()
        self.df = self.read_csv_sym(csv_type=self.ticker)
        for item in self.ta.ta_funcs:
            temp_df = self.read_csv_sym(csv_type=item)
            if not type(temp_df) == bool:
                self.df = pandas.concat([self.df, temp_df], axis=1)
        self.clean_df()

    def clean_df(self):
        '''
        Make all upper case
        Remove duplicate columns
        #Log duplicate columns, so eventually we don't generate them
        '''
        self.df.columns = [x.upper() for x in self.df.columns]
        self.df = self.df.T.groupby(level=0).first().T

    def clean_csv(self):
        self.exchange_from_ticker()
        for csv_type in self.ta.ta_funcs:
            fname = os.path.join(self.app_stores, self.exchange, self.ticker, csv_type + '.csv')
            try:
                tmp = ''
                with open(fname, 'r') as r:
                    tmp = r.readline()
                if "Date" not in tmp:
                    with open(fname, 'r+') as f:
                        line = 'Date'
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

    def save_all_precomputes_sql(self):
        #TODO add logging and timers
        #import database connector
        #drop table if exists? or update logic?
        for exchange, ticker in self.tickers:
            self.ticker = ticker
            #self.read_csv_sym()
            try:
                self.clean_csv()
            except:
                pass
            self.load_all_precomputes_csv()
            self.clean_df()
            self.save_df_sql()

from .stockDbSync import ManageTickers
from .PandasTALib import Abstract
import talib

manage_tickers = ManageTickers()
abstract = Abstractions(manage_tickers)
#I didn't want to do this, but I had to...
ta = Abstract(abstract, talib.abstract.__FUNCTION_NAMES)
abstract.ta = ta
