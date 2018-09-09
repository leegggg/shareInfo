from sqlalchemy import Column, String, create_engine, Integer, Float, Text, Date, DateTime
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from dateutil.parser import parse
from . import Base


def rowToORM(row, tablename):
    obj = TableCreator(tablename).KLine()
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

        code = Column(String(32), primary_key=True)  #  VDPP,
        ts = Column(DateTime, primary_key=True)
        open = Column(Float)  #  observation,
        close = Column(Float)  #  observation,
        high = Column(Float)  #  observation,
        low = Column(Float)  #  observation,
        volume = Column(Float)  #  observation,

    return KLine


def main():
    import tushare as ts
    from ..client.SqliteClient import SqliteClient
    dbclient = SqliteClient(base=Base, url='sqlite:///./test.db')
    # get_report_data(2017, 3, engine)
    # rep = ts.cap_tops()
    code = '600000'
    type = 'D'
    print(datetime.now())
    klines = ts.get_k_data(code=code, ktype=type)
    print(datetime.now())
    res = []
    for _, row in klines.iterrows():
        res.append(rowToORM(row, "k_{}_{}".format(code, type)))
    print(datetime.now())
    dbclient.save_all(res)
    print(datetime.now())


if __name__ == "__main__":
    main()