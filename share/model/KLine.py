from sqlalchemy import Column, String, create_engine, Integer, Float, Text, Date, DateTime
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from dateutil.parser import parse
from . import Base



def rowToORM(row, tablename):
    obj = TableCreator(tablename)()
    obj.code = row.loc['code']
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
        ts = Column(DateTime, primary_key=True)
        open = Column(Float)  #  observation,
        close = Column(Float)  #  observation,
        high = Column(Float)  #  observation,
        low = Column(Float)  #  observation,
        volume = Column(Float)  #  observation,

        def __init__(self):
            pass

    return KLine
