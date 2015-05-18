#!/usr/bin/env python3

import datetime, code, os, talib, pandas, csv
from talib import abstract
import numpy


class TargetAcquisition:
    '''
    This is where we can stack things to define our target set.

    Volume surge detection should definitely return AMD from Jan 17 Feb 4
    ...

    '''
    def __init__(self, abstractions):
        self.abstraction = abstractions

    def vol_price_move_reduction(self, df):
        pass

    def top_20_perc_price_moves_2_week(self, df):
        pass

class AdditionalPreComputes:
    '''
    ex:
    RollingVolMin - a way to inspect whether you want to play a particular position based on volume.

    Precompute the things to say:
    if trailing max > start + strike include in target set

    #This one is to say, we can't afford to exercise mid span, so it HAS to
    #close there two weeks out on friday.  This way automatic exercise rules
    #and auto-sell to cover the position on monday "just happen".  might want
    #to check the following monday price range to see if it's usually a wild
    #swing and we'll lose our shirt trying to sell it off.
    if monday close + strike >< close two weeks friday include in target set

    #we need a third precompute to tell us strike price indices in the current
    #market.  pandas has an API for this, but it is experimental.  otherwise,
    #we'll just rely on constants dicts.

    if rolling_volume > 100k include in target set

    Add these things to reduction a couple of reductionset items and make it
    a reductionsets item.  This way, we can find crossover between "Target set"
    and other reductionsets items.
    '''
    def __init__(self, abstractions):
        self.abstractions = abstractions
        self.func_dict = {'rol_avg':self.rol_avg}

    def rol_avg(self, df, key='volume', window=10):
        return pandas.rolling_mean(df[key], key, window)

    def high_low(self, df, window=10):
        pass

    def x_day_close(self, df, window=10):
        pass

    def opt_spread_prices(self):
        pass

    def precompute(self, df):
        for item in self.func_dict.keys():
            ret_vals = func_dict[item](df)
            self.abstractions.write_csv_sym(ret_vals, csv_type=item)

class ReductionSet:
    '''
    ex:
    Pattern is up down or reversal ??
    Compound -1 to +1 indicators and/or candles

    Each ReductionSet takes acceptable dates and a symbol as arguments.
    They must pull in dataframes to analyze around those acceptable dates.
    Finally, they must reduce the acceptable dates list and return a smaller
    or similarly sized list.

    This is here, so each reductionset can have its own lookback period.
    '''
    def __init__(self, abstractions):
        self.abstractions = abstractions

    def reduce(self, sym, dates):
        '''
        All subclasses should expose this method
        '''
        pass

class ReductionSets:
    '''
    Will probably be broken out in to a separate project.

    Takes a stack of ReductionSet and gives you the acceptable dates as output.
    '''
    def __init__(self, abstractions):
        self.abstractions = abstractions

    def set_reductions(self, reduction_set_list):
        '''
        All subclasses should expose this method
        '''
        pass

    def reduce(self, sym, dates):
        '''
        All subclasses should expose this method

        This next bit is pseudo-code.  It reads as what I want it to do.
        '''
        dates = dates # probably not necessary, I'll test removal eventually
        for item in self.reduction_set_list:
            dates = item(sym, dates)
        return dates

class Strategies:
    '''
    Will probably be broken out in to a smaller set of utilities.

    Uses ReductionSets to get window.

    Adds target entry and exit.
    '''
    def __init__(self, abstractions):
        self.abstractions = abstractions
    def gaps(self):
        pass
    def bollinger_pinch(self):
        pass
    def bollinger_breakout(self):
        pass
    def bolling_pinch_breakout_diff(self):
        '''
        Shorter windows between pinch and breakout should indicate higher volatility.
        '''
        pass
    def volume_spike(self):
        '''
        '''
        pass
    def ma_cross(self):
        '''
        '''
        pass

class Analysis:
    def __init__(self, abstractions):
        self.abstractions = abstractions
        self.additional_precomputes = AdditionalPreComputes(abstractions)
        self.reductions = ReductionSets(abstractions)
        self.strategies = Strategies(abstractions)