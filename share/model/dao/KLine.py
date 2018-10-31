from sqlalchemy import Column, String, Float, DateTime
from dateutil.parser import parse
from share.model.dao import Base
from share.util.numberUtil import toStr


def rowToORM(row, tablename, ktype):
    obj = TableCreator(tablename)()
    obj.code = toStr(row.loc['code'])
    obj.ktype = str(ktype)
    tsString = row.loc['date']
    datetime_object = parse(tsString)
    obj.ts = datetime_object
    obj.open = row.loc['open']
    obj.close = row.loc['close']
    obj.high = row.loc['high']
    obj.low = row.loc['low']
    obj.volume = row.loc['volume']
    return obj


def TableCreator(tablename):
    class KLine(Base):

        __tablename__ = tablename
        __table_args__ = {"useexisting": True}

        code = Column(String(32), primary_key=True)  #  VDPP,
        ktype = Column(String(32), primary_key=True)  # VDPP,
        ts = Column(DateTime, primary_key=True)
        open = Column(Float(53))  #  observation,
        close = Column(Float(53))  #  observation,
        high = Column(Float(53))  #  observation,
        low = Column(Float(53))  #  observation,
        volume = Column(Float(53))  #  observation,

        def __init__(self):
            pass

    return KLine
