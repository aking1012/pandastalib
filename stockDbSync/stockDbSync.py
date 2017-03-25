#!/usr/bin/env python3

import os, datetime, csv, urllib.request, multiprocessing, pandas
#import pandas.io.data as web
from pandas_datareader import data as web
#Classses to run the updates
class ManageEDGAR:
    '''
    A class to manage fundamental data from the SEC EDGAR database

    For the time being, it's just a placeholder...
    Also sort of like a to do statement.
    '''
    def __init__(self):
        pass

class ManageExchanges:
    '''
    A class to manage fetching all symbols for all exchanges
    '''
    def __init__(self):
        self.exchanges = [
        ('NASDAQ', 'http://www.nasdaq.com/screening/'+\
                             'companies-by-name.aspx?letter=0&exchange=nasdaq&render=download'),
        ('NYSE',     'http://www.nasdaq.com/screening/'+\
                             'companies-by-name.aspx?letter=0&exchange=nyse&render=download'),
        ('AMEX',     'http://www.nasdaq.com/screening/'+\
                             'companies-by-name.aspx?letter=0&exchange=amex&render=download')
        ]
        home = os.path.expanduser("~")
        self.app_stores = os.path.join(home, '.local', 'share', 'stockdb')
        os.makedirs(self.app_stores, exist_ok=True)
        self.curr_iter = 0

    def get_exchange_files(self, exchange_arg=False):
        '''
        A function to get all symbols for each exchange.
        Optionally provide an exchange_arg to only fetch symbols for a given exchange.
        '''
        for exchange in self.exchanges:
            if not exchange_arg:
                url = exchange[1]
            else:
                if exchange[0] == exchange_arg:
                    url = exchange[1]
                else:
                    continue
            req = urllib.request.Request(url, headers={'User-Agent' : "Derpy Browser"})
            csvfile = str(urllib.request.urlopen(req).read(), 'UTF-8').split('\r\n')
            write_to = os.path.join(self.app_stores, exchange[0] + '.csv')
            with open(write_to, 'w') as write_dest:
                for row in csvfile:
                    write_dest.write(row + '\n')

    def __iter__(self):
        return self

    def __next__(self):
        try:
            retval = self.exchanges[self.curr_iter]
        except IndexError:
            raise StopIteration
        self.curr_iter += 1
        return retval

class ManageTickers:
    '''
    A way to manage a pile of CSV files.
    '''
    def __init__(self):
        self.exchanges = ManageExchanges()
        self.curr_exchange = -1
        self.curr_ticker = -1
        self.exchanges_list = []
        self.syms = {}
        self.in_q = multiprocessing.Queue()
        self.out_q = multiprocessing.Queue()
        self.procs = []
        self.df = ''

        for exchange, url in self.exchanges:
            try:
                with open(os.path.join(self.exchanges.app_stores, exchange + '.csv'), "r") as my_file:
                    exchange_csv = csv.reader(my_file.readlines(), quotechar='"', delimiter=",")
                    self.exchanges_list.append(exchange)
                    temp = []
                    for item in exchange_csv:
                        try:
                            temp.append(item[0])
                        except IndexError:
                            pass
                    self.syms[exchange] = temp
            except FileNotFoundError:
                self.exchanges.get_exchange_files()
                with open(os.path.join(self.exchanges.app_stores, exchange + '.csv'), "r") as my_file:
                    exchange_csv = csv.reader(my_file.readlines(), quotechar='"', delimiter=",")
                    self.exchanges_list.append(exchange)
                    temp = []
                    for item in exchange_csv:
                        try:
                            temp.append(item[0])
                        except IndexError:
                            pass
                    self.syms[exchange] = temp


    def last_trading_day(self):
        '''
        Return a datetime object that holds the last trading day.
        '''
        today = datetime.datetime.today()
        today = today-datetime.timedelta(hours=(22))
        if today.weekday() > 4:
            today = today-datetime.timedelta(days=(6 - today.weekday()))
        return today

    def last_recorded_day(self, exchange, ticker):
        '''
        Return the last already fetched day as a datetime object.
        '''
        try:
            df = pandas.read_csv(os.path.join(self.exchanges.app_stores, exchange, ticker, ticker + '.csv'), index_col = 0)
            temp = df.last_valid_index().split('-')
            start_date = datetime.datetime(int(temp[0]), int(temp[1]), int(temp[2]))
            start_date = start_date+datetime.timedelta(days=(1))
        except OSError:
            start_date = datetime.datetime(1971, 2, 4)
        except IndexError:
            start_date = datetime.datetime(1971, 2, 4)
        return start_date

    def update(self, exchange, ticker):
        '''
        Exchange and ticker are required arguments now.  Side-effect of going multiprocessing
        '''
        sym = ticker
        today = self.last_trading_day()
        end_date = datetime.datetime(today.year, today.month, today.day)
        start_date = self.last_recorded_day(exchange, ticker)
        try:
            df = web.DataReader(ticker, 'yahoo', start_date, end_date)
            try:
                os.makedirs(os.path.join(self.exchanges.app_stores, exchange, ticker), exist_ok=True)
                with open(os.path.join(self.exchanges.app_stores, exchange, ticker, ticker + '.csv'), 'r') as old_data:
                    old_df = pandas.DataFrame.from_csv(old_data)
                    df = pandas.concat((old_df, df))
                with open(os.path.join(self.exchanges.app_stores, exchange, ticker, ticker + '.csv'), 'w') as questionable:
                    df.to_csv(questionable)
            except OSError:
                with open(os.path.join(self.exchanges.app_stores, exchange, ticker, ticker + '.csv'), 'w') as questionable:
                    df.to_csv(questionable)
        except OSError:
            pass


    def multi_update_target(self):
        '''
        The target function for multiprocessing updates
        '''
        while not self.in_q.empty():
            exchange, ticker = self.in_q.get()
            self.update(exchange, ticker)
            self.out_q.put((exchange, ticker))

    def multi_update(self, exchange=False, ticker=False):
        '''
        multiprocessing update for base data csv
        '''
        self.procs = []
        for i in range(multiprocessing.cpu_count()):
            self.procs.append(multiprocessing.Process(target=self.multi_update_target))
        if not ticker:
            for exchange, ticker in self:
                self.in_q.put((exchange, ticker))
        else:
            self.in_q.put((exchange, ticker))
        for proc in self.procs:
            proc.start()

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr_ticker == -1:
            self.curr_exchange +=1
        try:
            exch = self.exchanges_list[self.curr_exchange]
        except:
            self.curr_exchange = -1
            self.curr_ticker = -1
            raise StopIteration
        try:
            self.curr_ticker+=1
            sym = self.syms[self.exchanges_list[self.curr_exchange]][self.curr_ticker]
        except:
            self.curr_ticker = -1
            exch, sym = self.__next__()
        return(exch, sym)
