from sqlalchemy import Column, Integer, Float, Date, String, BigInteger
from share.model.dao import Base
from share.util.numberUtil import toFloat, toInt, toStr
from dateutil.parser import parse
import logging


def rowToORM(row):
    obj = Model()

    tsString = toStr(row.loc['opDate'])
    obj.opDate = None
    try:
        obj.opDate = parse(tsString)
    except:
        logging.warning("Fail to get date from {} from {}. Using {} as Fallback".
                        format(__name__, tsString, obj.opDate))

    obj.rzmre = toInt(row.loc['rzmre'])  # 融资买入额(元)
    obj.rzye = toInt(row.loc['rzye'])  # 融资余额(元)
    obj.rqmcl = toInt(row.loc['rqmcl'])  # 融券卖出量
    obj.rqyl = toInt(row.loc['rqyl'])  # 融券余量
    obj.rqye = toInt(row.loc['rqye'])  # 融券余量(元)
    obj.rzrqye = toInt(row.loc['rzrqye'])  # 融资融券余额(元)
    return obj


class Model(Base):
    # 表的名字:
    __tablename__ = 'REF_MARGIN_SZ'

    def __init__(self):
        pass

    # 表的结构:
    opDate = Column(Date, primary_key=True)  # 信用交易日期(index)
    rzmre = Column(BigInteger)  # 融资买入额(元)
    rzye = Column(BigInteger)  # 融资余额(元)
    rqmcl = Column(BigInteger)  # 融券卖出量
    rqyl = Column(BigInteger)  # 融券余量
    rqye = Column(BigInteger)  # 融券余量(元)
    rzrqye = Column(BigInteger)  # 融资融券余额(元)

