from talib import abstract
import multiprocessing, os, csv, pandas, numpy, datetime

#TODO need to play with os.nice

class PandasFunction(abstract.Function):
    def __init__(self, function_name):
        super().__init__(function_name)

    def set_input_arrays(self, input_data):
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
        super().set_input_arrays(input_data[names_lower].values)
        temp = input_data['volume'].values.astype('double')
        input_data['volume'] = temp
        return True

class PandasTALib:
    '''
    A class to hold abstractions to make TALib calls easier.

    Currently one argument to __init__ is abstractions.
    #TODO move this from a passed in argument to a relative import from util...
    '''
    def __init__(self, abstractions, ta_funcs):
        self.abstract = abstractions
        self.ta_funcs = ta_funcs
        self.in_q = multiprocessing.Queue()
        self.out_q = multiprocessing.Queue()
        self.procs = []
        self.got_first = False
        self.app_stores = self.abstract.app_stores
        self.ticker = ''
        self.exchange = ''

    def read_csv_sym(self, csv_type=False, ticker=False, exchange=False):
        self.ticker = ticker
        self.exchange = exchange
        fname = os.path.join(self.app_stores, exchange, ticker, csv_type + '.csv')
        try:
            return pandas.read_csv(fname, index_col=0, sep=',', quotechar='"', header='infer', low_memory=True, parse_dates=True, infer_datetime_format=True)
        except:
            return False

    def precompute(self, exchange, ticker):
        print('precomputing ' + ticker)
        data = self.read_csv_sym(ticker, ticker, exchange)
        try:
            if not data: return
        except ValueError as e:
            #This catches the error for when data would normally pythonically be True.
            #However, dataframes don't like the if exists True operation/trick and
            #  throw a ValueError instead.
            e = e
        for item in self.ta_funcs:
            if item == 'MAVP':
                #Added bonus, we don't have to probe for inputs.  A frame works
                #all across the board.
                continue
                #TODO trim extra precomputes - MIN and MAX are computed twice etc...
            temp_func = PandasFunction(item)
            #in progress
            append = True
            #Get so far already done
            try:
                precomp = pandas.read_csv(os.path.join(self.app_stores, exchange, ticker, item + '.csv'), header=None, names=['Date', '0'], index_col = 0)
                start_date = precomp.last_valid_index()
            except OSError:
                append = False
                start_date = str(datetime.datetime(1971, 2, 4))
            except IndexError:
                append = False
                start_date = str(datetime.datetime(1971, 2, 4))
            #Get lookback
            lookback = temp_func.lookback + 1

            try:
                #Slice data to only include lookback required dates
                index_compute_end = numpy.where(precomp.index==start_date)[0][0]
            except IndexError:
                index_compute_end = 0
            except UnboundLocalError:
                index_compute_end = 0

            if index_compute_end > lookback:
                index_compute_start = index_compute_end - lookback
            else:
                index_compute_start = 0
            sliced_input = data.iloc[index_compute_start:-1]

            try:
                #TODO Need to figure out why it pukes if I don't call this twice...
                #might have fixed that... need to test.
                #temp_func.set_input_arrays(data)
                #temp_func.set_input_arrays(data)
                temp_func.set_input_arrays(sliced_input)
                temp_func.set_input_arrays(sliced_input)

                #Compute
                try:
                    frame = temp_func()
                except:
                    continue

                #Chop off lookback from start of output

                try:
                    frame = frame.iloc[lookback-1:-1]
                except IndexError:
                    continue
                try:
                    index_compute_end = numpy.where(frame.index==start_date)[0][0]
                    sliced_output = frame.iloc[index_compute_end+1:].copy()
                except IndexError:
                    pass
                except UnboundLocalError:
                    df = frame
                except:
                    #If it's a new fetch, it can't find a date, so write the whole frame
                    append = False
                if (append):
                    print('Trying to append')
                    with open(os.path.join(self.app_stores, exchange, ticker, item + '.csv'), 'a') as fname:
                        sliced_output.to_csv(fname)
                else:
                    with open(os.path.join(self.app_stores, exchange, ticker, item + '.csv'), 'w') as fname:
                        frame.to_csv(fname)
            except TypeError as e:
                print('Type mismatch on: ' + ticker)

    def multi_precompute_target(self):
        '''
        The target function for multiprocessing updates
        '''
        while (not self.in_q.empty()) or (not self.got_first):
            exchange, ticker = self.in_q.get()
            self.got_first = True
            self.precompute(exchange, ticker)
            self.out_q.put((exchange, ticker))


    def multi_precompute(self):
        '''
        multiprocessing update for base data csv
        '''
        self.procs = []
        for i in range(multiprocessing.cpu_count()):
            self.procs.append(multiprocessing.Process(target=self.multi_precompute_target))
        for proc in self.procs:
            proc.start()