#!/usr/bin/env python3

import os, datetime, csv, urllib.request, multiprocessing, pandas
import pandas.io.data as web

#Classses to run the updates
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
        #TODO Add logic for after 22:00 syncs and make computation fast enough that this is done before I wake up.
        today = today-datetime.timedelta(days=(1))
        if today.weekday() > 4:
            today = today-datetime.timedelta(days=(6 - today.weekday()))
        return today

    def last_recorded_day(self, exchange, ticker):
        '''
        Return the last already fetched day as a datetime object.
        '''
        try:
            df = pandas.read_csv(os.path.join(self.exchanges.app_stores, exchange, ticker, ticker + '.csv'), index_col = 0)
            #TODO set start date for fetch
        except OSError:
            start_date = False
        return False

    def update(self, exchange, ticker):
        '''
        Exchange and ticker are required arguments now.  Side-effect of going multiprocessing
        '''

        sym = ticker
        today = self.last_trading_day()
        end_date = datetime.datetime(today.year, today.month, today.day)
        start_date = datetime.datetime(1971, 2, 4)
        #TODO get name of exception with a test run...
        temp_start = self.last_recorded_day(exchange, ticker)
        if temp_start:
            start_date = temp_start

        try:
            df = web.DataReader(ticker, 'yahoo', start_date, end_date)
            os.makedirs(os.path.join(self.exchanges.app_stores, exchange, ticker), exist_ok=True)
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

    def multi_update(self):
        '''
        multiprocessing update for base data csv
        '''
        self.procs = []
        for i in range(multiprocessing.cpu_count()):
            self.procs.append(multiprocessing.Process(target=self.multi_update_target))
        for exchange, ticker in self:
            self.in_q.put((exchange, ticker))
        for proc in self.procs:
            proc.start()
        #Well, multiproc updates is faster, but it blocks on join as implemented...
        #for proc in self.procs:
        #    proc.join()
        #self.procs = []
        #For now, I just have a couple of procs that live even though they should die.
        #Just forces me to implement concurrent precomputes and force proc kills
        #instead of using join.

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
