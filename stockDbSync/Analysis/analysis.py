#The next several classes are just scaffolds with descriptions about how
#  I intend to use them.
class AdditionalPreComputes:
    '''
    ex:
    Trailing 10 trading day high-low(identify price leaps for possible entry or exit candidates)
    Trailing 20 trading day high-low(identify price leaps for possible entry or exit candidates)
    Trailing 25 trading day high-low(identify price leaps for possible entry or exit candidates)
    RollingVolAvg - a way to inspect whether you want to play a particular position based on volume.
    '''
    def __init__(self, abstractions):
        self.abstractions = abstractions

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

class ReductionSets:
    '''
    Will probably be broken out in to a separate project.

    Takes a stack of ReductionSet and gives you the acceptable dates as output.
    '''
    def __init__(self, abstractions):
        self.abstractions = abstractions

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



class Analysis:
    def __init__(self, abstractions):
        self.abstractions = abstractions
        self.additional_precomputes = AdditionalPreComputes(abstractions)
        self.reduction = ReductionSet(abstractions)
        self.reductions = ReductionSets(abstractions)
        self.strategies = Strategies(abstractions)
