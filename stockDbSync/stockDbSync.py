#!/usr/bin/env python3

#TODO add threading/multiprocessing for fetches...

import os, datetime, csv

#Ignore the pylint warning here...
try:
    import urllib.request
except ImportError:
    import urllib

import pandas.io.data as web

#Classses to run the updates
#TODO move the things that use the functions instead of the iterators to iterators...

class ManageExchanges:
    '''
    A class to manage fetching all symbols for all exchanges
    '''
    def __init__(self):
        '''
        A list of CSV links to get symbols for all exchanges
        '''
        self.exchanges = [
        ('NASDAQ', 'http://www.nasdaq.com/screening/'+\
                             'companies-by-name.aspx?letter=0&exchange=nasdaq&render=download'),
        ('NYSE',     'http://www.nasdaq.com/screening/'+\
                             'companies-by-name.aspx?letter=0&exchange=nyse&render=download'),
        ('AMEX',     'http://www.nasdaq.com/screening/'+\
                             'companies-by-name.aspx?letter=0&exchange=amex&render=download')
        ]
        home = os.path.expanduser("~")
        self.app_stores = os.path.join(home, '.config', 'stockdb')
        #pylint misfires on this one...
        os.makedirs(self.app_stores, exist_ok=True)
        self.curr_iter = 0

    def get_syms(self, exchange_arg=False):
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
            #and here...
            req = urllib.request.Request(url, headers={'User-Agent' : "Derpy Browser"})
            csvfile = str(urllib.request.urlopen(req).read(), 'UTF-8').split('\r\n')
            write_to = os.path.join(self.app_stores, exchange[0] + '.csv')
            with open(write_to, 'w') as write_dest:
                for row in csvfile:
                    write_dest.write(row + '\n')

    def exchanges_list(self):
        '''
        A generator for a list of exchanges
        '''
        for item in self.exchanges:
            try:
                yield(item)
            except:
                #I know it's nasty to have catch-alls
                pass

    def tickers(self, exchange):
        '''
        A generator for a list of tickers
        '''
        with open(os.path.join(self.app_stores, exchange[0] + '.csv'), "r") as my_file:
            exchange_csv = csv.reader(my_file.readlines(), quotechar='"', delimiter=",")
            for item in exchange_csv:
                try:
                    yield(item[0])
                except:
                    #I know it's nasty to have catch-alls
                    pass

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
        '''
        Nothing going on here, move along...
        '''
        self.exchanges = ManageExchanges()
        self.curr_exchange = -1
        self.curr_ticker = -1
        self.exchanges_list = []
        self.syms = {}
        for exchange, url in self.exchanges:
            with open(os.path.join(self.exchanges.app_stores, exchange + '.csv'), "r") as my_file:
                exchange_csv = csv.reader(my_file.readlines(), quotechar='"', delimiter=",")
                self.exchanges_list.append(exchange)
                temp = []
                for item in exchange_csv:
                    try:
                        temp.append(item[0])
                    except:
                        #I know it's nasty to have catch-alls
                        pass
                self.syms[exchange] = temp

    def last_trading_day(self):
        '''
        Return a datetime object that holds the last trading day.
        '''
        today = datetime.datetime.today()
        #Add logic for after five syncs
        today = today-datetime.timedelta(days=(1))
        if today.weekday() > 4:
            today = today-datetime.timedelta(days=(6 - today.weekday()))
        return today

    def update(self, exchange=False, ticker=False):
        '''
        The name says it all...    takes the optional arguments exchange and ticker.

        If you specify an exchange, it should only iterate over that exchange.
        If you specify a ticker, it should only update that ticker.

        If you specify nothing, it should update the whole CSV blob set.
        '''
        sym = ticker
        today = self.last_trading_day()
        end_date = (today.year, today.month, today.day)
        end_date = datetime.datetime(end_date[0], end_date[1], end_date[2])
        for exchange in self.exchanges.exchanges:
            for ticker in self.exchanges.tickers(exchange):
                start_date = datetime.datetime(1971, 2, 4)
                #TODO find last date from CSV
                #might wind up not caring about that though...  need to time it.
                #
                #if os.path.exists(os.path.join(self.exchanges.app_stores, ticker, ticker + 'csv')):
                #    df = pandas.read_csv(os.path.join(self.exchanges.app_stores, exchange[0], ticker, ticker + '.csv'), index_col = 0)
                #    This will happen later, much later.

                #pylint misfire
                os.makedirs(os.path.join(self.exchanges.app_stores, exchange[0], ticker), exist_ok=True)
                try:
                    with open(os.path.join(self.exchanges.app_stores, exchange[0], ticker, ticker + '.csv'), 'w') as questionable:
                        if (not sym) or (ticker == sym):
                            df = web.DataReader(ticker, 'yahoo', start_date, end_date)
                            df.to_csv(questionable)
                except:
                    #I know it's nasty to have catch-alls
                    pass

    def __iter__(self):
        return self

    def __next__(self):
        #TODO not iterating...
        #Handle exchange iter
        if self.curr_ticker == -1:
            self.curr_exchange +=1
        try:
            exch = self.exchanges_list[self.curr_exchange]
        except:
            self.curr_exchange = -1
            self.curr_ticker = -1
            raise StopIteration
        #Handle sym iter
        try:
            self.curr_ticker+=1
            sym = self.syms[self.exchanges_list[self.curr_exchange]][self.curr_ticker]
        except:
            self.curr_ticker = -1
            exch, sym = self.__next__()
        return(exch, sym)
