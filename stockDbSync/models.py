"""
Defines a table to force that talib and other
precomputes I'm using in to a table.
"""

from flask import Flask

import sqlalchemy as SQLAlchemy
#from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
#db = SQLAlchemy(app)

class StockTick(db.Model):
    '''
    A class to help convert a massive set of pandas precomputes dfs to sql records,
    and read them back out with Flask.

    Also for use in minimal flask dashboards
    '''
    __tablename__ = 'base_precomputes'

    #Precomputes for
    ACOS = db.Column(db.Float)
    AD = db.Column(db.Float)
    ADD = db.Column(db.Float)
    ADOSC = db.Column(db.Float)
    ADX = db.Column(db.Float)
    ADXR = db.Column(db.Float)
    APO = db.Column(db.Float)
    AROONDOWN = db.Column(db.Float)
    AROONOSC = db.Column(db.Float)
    AROONUP = db.Column(db.Float)
    ASIN = db.Column(db.Float)
    ATAN = db.Column(db.Float)
    ATR = db.Column(db.Float)
    AVGPRICE = db.Column(db.Float)
    BETA = db.Column(db.Float)

    #bollinger
    LOWERBAND = db.Column(db.Float)
    MIDDLEBAND = db.Column(db.Float)
    UPPERBAND = db.Column(db.Float)

    BOP = db.Column(db.Float)
    CCI = db.Column(db.Float)

    #Candlesticks
    CDL2CROWS = db.Column(db.Integer)
    CDL3BLACKCROWS = db.Column(db.Integer)
    CDL3INSIDE = db.Column(db.Integer)
    CDL3LINESTRIKE = db.Column(db.Integer)
    CDL3OUTSIDE = db.Column(db.Integer)
    CDL3STARSINSOUTH = db.Column(db.Integer)
    CDL3WHITESOLDIERS = db.Column(db.Integer)
    CDLABANDONEDBABY = db.Column(db.Integer)
    CDLADVANCEBLOCK = db.Column(db.Integer)
    CDLBELTHOLD = db.Column(db.Integer)
    CDLBREAKAWAY = db.Column(db.Integer)
    CDLCLOSINGMARUBOZU = db.Column(db.Integer)
    CDLCONCEALBABYSWALL = db.Column(db.Integer)
    CDLCOUNTERATTACK = db.Column(db.Integer)
    CDLDARKCLOUDCOVER = db.Column(db.Integer)
    CDLDOJI = db.Column(db.Integer)
    CDLDOJISTAR = db.Column(db.Integer)
    CDLDRAGONFLYDOJI = db.Column(db.Integer)
    CDLENGULFING = db.Column(db.Integer)
    CDLEVENINGDOJISTAR = db.Column(db.Integer)
    CDLEVENINGSTAR = db.Column(db.Integer)
    CDLGAPSIDESIDEWHITE = db.Column(db.Integer)
    CDLGRAVESTONEDOJI = db.Column(db.Integer)
    CDLHAMMER = db.Column(db.Integer)
    CDLHANGINGMAN = db.Column(db.Integer)
    CDLHARAMI = db.Column(db.Integer)
    CDLHARAMICROSS = db.Column(db.Integer)
    CDLHIGHWAVE = db.Column(db.Integer)
    CDLHIKKAKE = db.Column(db.Integer)
    CDLHIKKAKEMOD = db.Column(db.Integer)
    CDLHOMINGPIGEON = db.Column(db.Integer)
    CDLIDENTICAL3CROWS = db.Column(db.Integer)
    CDLINNECK = db.Column(db.Integer)
    CDLINVERTEDHAMMER = db.Column(db.Integer)
    CDLKICKING = db.Column(db.Integer)
    CDLKICKINGBYLENGTH = db.Column(db.Integer)
    CDLLADDERBOTTOM = db.Column(db.Integer)
    CDLLONGLEGGEDDOJI = db.Column(db.Integer)
    CDLLONGLINE = db.Column(db.Integer)
    CDLMARUBOZU = db.Column(db.Integer)
    CDLMATCHINGLOW = db.Column(db.Integer)
    CDLMATHOLD = db.Column(db.Integer)
    CDLMORNINGDOJISTAR = db.Column(db.Integer)
    CDLMORNINGSTAR = db.Column(db.Integer)
    CDLONNECK = db.Column(db.Integer)
    CDLPIERCING = db.Column(db.Integer)
    CDLRICKSHAWMAN = db.Column(db.Integer)
    CDLRISEFALL3METHODS = db.Column(db.Integer)
    CDLSEPARATINGLINES = db.Column(db.Integer)
    CDLSHOOTINGSTAR = db.Column(db.Integer)
    CDLSHORTLINE = db.Column(db.Integer)
    CDLSPINNINGTOP = db.Column(db.Integer)
    CDLSTALLEDPATTERN = db.Column(db.Integer)
    CDLSTICKSANDWICH = db.Column(db.Integer)
    CDLTAKURI = db.Column(db.Integer)
    CDLTASUKIGAP = db.Column(db.Integer)
    CDLTHRUSTING = db.Column(db.Integer)
    CDLTRISTAR = db.Column(db.Integer)
    CDLUNIQUE3RIVER = db.Column(db.Integer)
    CDLUPSIDEGAP2CROWS = db.Column(db.Integer)
    CDLXSIDEGAP3METHODS = db.Column(db.Integer)

    CEIL = db.Column(db.Float)
    CMO = db.Column(db.Float)
    CORREL = db.Column(db.Float)
    COS = db.Column(db.Float)
    COSH = db.Column(db.Float)
    DEMA = db.Column(db.Float)
    DIV = db.Column(db.Float)
    DX = db.Column(db.Float)
    EMA = db.Column(db.Float)
    EXP = db.Column(db.Float)
    FAMA = db.Column(db.Float)
    FLOOR = db.Column(db.Float)
    HT_DCPERIOD = db.Column(db.Float)
    HT_DCPHASE = db.Column(db.Float)
    HT_TRENDLINE = db.Column(db.Float)
    HT_TRENDMODE = db.Column(db.Float)
    INPHASE = db.Column(db.Float)

    #IDX
    MAXIDX = db.Column(db.Float)
    MINIDX = db.Column(db.Float)

    KAMA = db.Column(db.Float)

    #FastK SlowK
    FASTD = db.Column(db.Float)
    FASTK = db.Column(db.Float)
    SLOWD = db.Column(db.Float)
    SLOWK = db.Column(db.Float)

    LEADSINE = db.Column(db.Float)
    LINEARREG = db.Column(db.Float)
    LINEARREG_ANGLE = db.Column(db.Float)
    LINEARREG_INTERCEPT = db.Column(db.Float)
    LINEARREG_SLOPE = db.Column(db.Float)
    LN = db.Column(db.Float)
    LOG10 = db.Column(db.Float)
    MA = db.Column(db.Float)

    MACD = db.Column(db.Float)
    MACDHIST = db.Column(db.Float)
    MACDSIGNAL = db.Column(db.Float)

    MAMA = db.Column(db.Float)

    #MinMax
    MAX = db.Column(db.Float)
    MIN = db.Column(db.Float)

    MAXINDEX = db.Column(db.Float)
    MEDPRICE = db.Column(db.Float)
    MFI = db.Column(db.Float)
    MIDPOINT = db.Column(db.Float)
    MIDPRICE = db.Column(db.Float)
    MININDEX = db.Column(db.Float)
    MINUS_DI = db.Column(db.Float)
    MINUS_DM = db.Column(db.Float)
    MOM = db.Column(db.Float)
    MULT = db.Column(db.Float)
    NATR = db.Column(db.Float)
    OBV = db.Column(db.Float)
    PLUS_DI = db.Column(db.Float)
    PLUS_DM = db.Column(db.Float)
    PPO = db.Column(db.Float)
    QUADRATURE = db.Column(db.Float)
    ROC = db.Column(db.Float)
    ROCP = db.Column(db.Integer)
    ROCR = db.Column(db.Float)
    ROCR100 = db.Column(db.Float)
    RSI = db.Column(db.Float)
    SAR = db.Column(db.Float)
    SAREXT = db.Column(db.Float)
    SIN = db.Column(db.Float)
    SINE = db.Column(db.Float)
    SINH = db.Column(db.Float)
    SMA = db.Column(db.Float)
    SQRT = db.Column(db.Float)
    STDDEV = db.Column(db.Float)
    SUB = db.Column(db.Float)
    SUM = db.Column(db.Float)
    T3 = db.Column(db.Float)
    TAN = db.Column(db.Float)
    TANH = db.Column(db.Integer)
    TEMA = db.Column(db.Float)
    TRANGE = db.Column(db.Float)
    TRIMA = db.Column(db.Float)
    TRIX = db.Column(db.Float)
    TSF = db.Column(db.Float)
    TYPPRICE = db.Column(db.Float)
    ULTOSC = db.Column(db.Float)
    VAR = db.Column(db.Float)
    WCLPRICE = db.Column(db.Float)
    WILLR = db.Column(db.Float)
    WMA = db.Column(db.Float)

    #Part of the composite primary key
    DATE = db.Column(db.DateTime, primary_key=True)

    #Added field, so it can be one huge flat table
    #other part of composite primary key
    TICKER = db.Column(db.String(10), primary_key=True)

    #Addd field for exchange traded upon
    EXCHANGE = db.Column(db.String(10))

    #Added fields to put things like price moves as percentages

    def __init__(self, index, row, exchange):
        #TODDO add an attr iter
        self.ACOS = row['ACOS']
        self.AD = row['AD']
        self.ADD = row['ADD']
        self.ADOSC = row['ADOSC']
        self.ADX = row['ADX']
        self.ADXR = row['ADXR']
        self.APO = row['APO']
        self.AROONDOWN = row['AROONDOWN']
        self.AROONOSC = row['AROONOSC']
        self.AROONUP = row['AROONUP']
        self.ASIN = row['ASIN']
        self.ATAN = row['ATAN']
        self.ATR = row['ATR']
        self.AVGPRICE = row['AVGPRICE']
        self.BETA = row['BETA']
        self.LOWERBAND = row['LOWERBAND']
        self.MIDDLEBAND = row['MIDDLEBAND']
        self.UPPERBAND = row['UPPERBAND']
        self.BOP = row['BOP']
        self.CCI = row['CCI']
        self.CDL2CROWS = row['CDL2CROWS']
        self.CDL3BLACKCROWS = row['CDL3BLACKCROWS']
        self.CDL3INSIDE = row['CDL3INSIDE']
        self.CDL3LINESTRIKE = row['CDL3LINESTRIKE']
        self.CDL3OUTSIDE = row['CDL3OUTSIDE']
        self.CDL3STARSINSOUTH = row['CDL3STARSINSOUTH']
        self.CDL3WHITESOLDIERS = row['CDL3WHITESOLDIERS']
        self.CDLABANDONEDBABY = row['CDLABANDONEDBABY']
        self.CDLADVANCEBLOCK = row['CDLADVANCEBLOCK']
        self.CDLBELTHOLD = row['CDLBELTHOLD']
        self.CDLBREAKAWAY = row['CDLBREAKAWAY']
        self.CDLCLOSINGMARUBOZU = row['CDLCLOSINGMARUBOZU']
        self.CDLCONCEALBABYSWALL = row['CDLCONCEALBABYSWALL']
        self.CDLCOUNTERATTACK = row['CDLCOUNTERATTACK']
        self.CDLDARKCLOUDCOVER = row['CDLDARKCLOUDCOVER']
        self.CDLDOJI = row['CDLDOJI']
        self.CDLDOJISTAR = row['CDLDOJISTAR']
        self.CDLDRAGONFLYDOJI = row['CDLDRAGONFLYDOJI']
        self.CDLENGULFING = row['CDLENGULFING']
        self.CDLEVENINGDOJISTAR = row['CDLEVENINGDOJISTAR']
        self.CDLEVENINGSTAR = row['CDLEVENINGSTAR']
        self.CDLGAPSIDESIDEWHITE = row['CDLGAPSIDESIDEWHITE']
        self.CDLGRAVESTONEDOJI = row['CDLGRAVESTONEDOJI']
        self.CDLHAMMER = row['CDLHAMMER']
        self.CDLHANGINGMAN = row['CDLHANGINGMAN']
        self.CDLHARAMI = row['CDLHARAMI']
        self.CDLHARAMICROSS = row['CDLHARAMICROSS']
        self.CDLHIGHWAVE = row['CDLHIGHWAVE']
        self.CDLHIKKAKE = row['CDLHIKKAKE']
        self.CDLHIKKAKEMOD = row['CDLHIKKAKEMOD']
        self.CDLHOMINGPIGEON = row['CDLHOMINGPIGEON']
        self.CDLIDENTICAL3CROWS = row['CDLIDENTICAL3CROWS']
        self.CDLINNECK = row['CDLINNECK']
        self.CDLINVERTEDHAMMER = row['CDLINVERTEDHAMMER']
        self.CDLKICKING = row['CDLKICKING']
        self.CDLKICKINGBYLENGTH = row['CDLKICKINGBYLENGTH']
        self.CDLLADDERBOTTOM = row['CDLLADDERBOTTOM']
        self.CDLLONGLEGGEDDOJI = row['CDLLONGLEGGEDDOJI']
        self.CDLLONGLINE = row['CDLLONGLINE']
        self.CDLMARUBOZU = row['CDLMARUBOZU']
        self.CDLMATCHINGLOW = row['CDLMATCHINGLOW']
        self.CDLMATHOLD = row['CDLMATHOLD']
        self.CDLMORNINGDOJISTAR = row['CDLMORNINGDOJISTAR']
        self.CDLMORNINGSTAR = row['CDLMORNINGSTAR']
        self.CDLONNECK = row['CDLONNECK']
        self.CDLPIERCING = row['CDLPIERCING']
        self.CDLRICKSHAWMAN = row['CDLRICKSHAWMAN']
        self.CDLRISEFALL3METHODS = row['CDLRISEFALL3METHODS']
        self.CDLSEPARATINGLINES = row['CDLSEPARATINGLINES']
        self.CDLSHOOTINGSTAR = row['CDLSHOOTINGSTAR']
        self.CDLSHORTLINE = row['CDLSHORTLINE']
        self.CDLSPINNINGTOP = row['CDLSPINNINGTOP']
        self.CDLSTALLEDPATTERN = row['CDLSTALLEDPATTERN']
        self.CDLSTICKSANDWICH = row['CDLSTICKSANDWICH']
        self.CDLTAKURI = row['CDLTAKURI']
        self.CDLTASUKIGAP = row['CDLTASUKIGAP']
        self.CDLTHRUSTING = row['CDLTHRUSTING']
        self.CDLTRISTAR = row['CDLTRISTAR']
        self.CDLUNIQUE3RIVER = row['CDLUNIQUE3RIVER']
        self.CDLUPSIDEGAP2CROWS = row['CDLUPSIDEGAP2CROWS']
        self.CDLXSIDEGAP3METHODS = row['CDLXSIDEGAP3METHODS']
        self.CEIL = row['CEIL']
        self.CMO = row['CMO']
        self.CORREL = row['CORREL']
        self.COS = row['COS']
        self.COSH = row['COSH']
        self.DEMA = row['DEMA']
        self.DIV = row['DIV']
        self.DX = row['DX']
        self.EMA = row['EMA']
        self.EXP = row['EXP']
        self.FAMA = row['FAMA']
        self.FLOOR = row['FLOOR']
        self.HT_DCPERIOD = row['HT_DCPERIOD']
        self.HT_DCPHASE = row['HT_DCPHASE']
        self.HT_TRENDLINE = row['HT_TRENDLINE']
        self.HT_TRENDMODE = row['HT_TRENDMODE']
        self.INPHASE = row['INPHASE']
        self.MAXIDX = row['MAXIDX']
        self.MINIDX = row['MINIDX']
        self.KAMA = row['KAMA']
        self.FASTD = row['FASTD']
        self.FASTK = row['FASTK']
        self.SLOWD = row['SLOWD']
        self.SLOWK = row['SLOWK']
        self.LEADSINE = row['LEADSINE']
        self.LINEARREG = row['LINEARREG']
        self.LINEARREG_ANGLE = row['LINEARREG_ANGLE']
        self.LINEARREG_INTERCEPT = row['LINEARREG_INTERCEPT']
        self.LINEARREG_SLOPE = row['LINEARREG_SLOPE']
        self.LN = row['LN']
        self.LOG10 = row['LOG10']
        self.MA = row['MA']
        self.MACD = row['MACD']
        self.MACDHIST = row['MACDHIST']
        self.MACDSIGNAL = row['MACDSIGNAL']
        self.MAMA = row['MAMA']
        self.MAX = row['MAX']
        self.MIN = row['MIN']
        self.MAXINDEX = row['MAXINDEX']
        self.MEDPRICE = row['MEDPRICE']
        self.MFI = row['MFI']
        self.MIDPOINT = row['MIDPOINT']
        self.MIDPRICE = row['MIDPRICE']
        self.MININDEX = row['MININDEX']
        self.MINUS_DI = row['MINUS_DI']
        self.MINUS_DM = row['MINUS_DM']
        self.MOM = row['MOM']
        self.MULT = row['MULT']
        self.NATR = row['NATR']
        self.OBV = row['OBV']
        self.PLUS_DI = row['PLUS_DI']
        self.PLUS_DM = row['PLUS_DM']
        self.PPO = row['PPO']
        self.QUADRATURE = row['QUADRATURE']
        self.ROC = row['ROC']
        self.ROCP = row['ROCP']
        self.ROCR = row['ROCR']
        self.ROCR100 = row['ROCR100']
        self.RSI = row['RSI']
        self.SAR = row['SAR']
        self.SAREXT = row['SAREXT']
        self.SIN = row['SIN']
        self.SINE = row['SINE']
        self.SINH = row['SINH']
        self.SMA = row['SMA']
        self.SQRT = row['SQRT']
        self.STDDEV = row['STDDEV']
        self.SUB = row['SUB']
        self.SUM = row['SUM']
        self.T3 = row['T3']
        self.TAN = row['TAN']
        self.TANH = row['TANH']
        self.TEMA = row['TEMA']
        self.TRANGE = row['TRANGE']
        self.TRIMA = row['TRIMA']
        self.TRIX = row['TRIX']
        self.TSF = row['TSF']
        self.TYPPRICE = row['TYPPRICE']
        self.ULTOSC = row['ULTOSC']
        self.VAR = row['VAR']
        self.WCLPRICE = row['WCLPRICE']
        self.WILLR = row['WILLR']
        self.WMA = row['WMA']
        self.TICKER = row['TICKER']

        self.EXCHANGE = exchange
        self.DATE = index

    def junk_method(self):
        import inspect

        def props(obj):
            pr = {}
            for name in dir(obj):
                value = getattr(obj, name)
                if not name.startswith('__') and not inspect.ismethod(value):
                    pr[name] = value
            return pr

    def insert_sqlalchemy_core(self):
        engine.execute(
            self.__table__.insert(),
            [{"name": 'NAME ' + str(i)} for i in range(n)]
        )

    def __repr__(self):
        return 'Not implemented'


class StockTicks:
    '''
    A class to take a df and iter over rows to do the migration to SQL
    '''
    def __init__(self, df):
        self.df = df
     #TODO here...
    def test_sqlalchemy_core(self, n=100000):
        engine.execute(
            StockTick.__table__.insert(),
            [{"name": 'NAME ' + str(i)} for i in range(n)]
            )
        print("SQLAlchemy Core: Total time for " + str(n) +
            " records " + str(time.time() - t0) + " secs")

'''
import time
import sqlite3

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,  create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()
DBSession = scoped_session(sessionmaker())
engine = None

class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

def init_sqlalchemy(dbname='sqlite:///sqlalchemy.db'):
    global engine
    engine = create_engine(dbname, echo=False)
    DBSession.remove()
    DBSession.configure(bind=engine, autoflush=False, expire_on_commit=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def test_sqlalchemy_core(n=100000):
    init_sqlalchemy()
    t0 = time.time()
    engine.execute(
        Customer.__table__.insert(),
        [{"name": 'NAME ' + str(i)} for i in range(n)]
    )
    print("SQLAlchemy Core: Total time for " + str(n) +
        " records " + str(time.time() - t0) + " secs")
'''