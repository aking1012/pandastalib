from talib import abstract

#Still have to inspect and group for the organized abstract API

class PandasFunction(abstract.Function):
    def __init__(self, function_name):
        '''
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
        self.abstractions = abstractions
        self.ta_funcs = ta_funcs

    def precompute(self, ticker, exchange=False, category=False):
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
