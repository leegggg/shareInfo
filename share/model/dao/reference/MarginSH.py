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

    obj.rzye = toInt(row.loc['rzye'])  # 本日融资余额(元)
    obj.rzmre = toInt(row.loc['rzmre'])  # 本日融资买入额(元)
    obj.rqyl = toInt(row.loc['rqyl'])  # 本日融券余量
    obj.rqylje = toInt(row.loc['rqylje'])  # 本日融券余量金额(元)
    obj.rqmcl = toInt(row.loc['rqmcl'])  # 本日融券卖出量
    obj.rzrqjyzl = toInt(row.loc['rzrqjyzl'])  # 本日融资融券余额(元)
    return obj


class Model(Base):
    # 表的名字:
    __tablename__ = 'REF_MARGIN_SH'

    def __init__(self):
        pass

    # 表的结构:
    opDate = Column(Date, primary_key=True)  # 信用交易日期(index)
    rzye = Column()  # 本日融资余额(元)
    rzmre = Column(BigInteger)  # 本日融资买入额(元)
    rqyl = Column(BigInteger)  # 本日融券余量
    rqylje = Column(BigInteger)  # 本日融券余量金额(元)
    rqmcl = Column(BigInteger)  # 本日融券卖出量
    rzrqjyzl = Column(BigInteger)  # 本日融资融券余额(元)

