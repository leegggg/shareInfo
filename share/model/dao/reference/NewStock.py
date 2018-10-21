from sqlalchemy import Column, Integer, Float, Date, String, BigInteger
from share.model.dao import Base
from share.util.numberUtil import toFloat, toInt
from datetime import datetime
from dateutil.parser import parse
import logging


def rowToORM(row):
    obj = Model()

    obj.code = str(row.loc['code'])  # 股票代码
    obj.name = str(row.loc['name'])  # 股票名称

    obj.date = datetime.now()

    tsString = str(row.loc['ipo_date'])
    obj.ipo_date = None
    try:
        obj.ipo_date = parse(tsString)
    except:
        logging.warning("Fail to get date from {} from {}. Using {} as Fallback".
                        format(__name__, tsString, obj.ipo_date))

    tsString = str(row.loc['issue_date'])
    obj.issue_date = None
    try:
        obj.issue_date = parse(tsString)
    except:
        logging.warning("Fail to get date from {} from {}. Using {} as Fallback".
                        format(__name__, tsString, obj.issue_date))

    if obj.code is None or obj.ipo_date is None:
        return None

    obj.amount = toInt(row.loc['amount'])  # 发行数量(万股)
    obj.markets = toInt(row.loc['markets'])  # 上网发行数量(万股)
    obj.price = toFloat(row.loc['price'])  # 发行价格(元)
    obj.pe = toFloat(row.loc['pe'])  # 发行市盈率
    obj.limit = toFloat(row.loc['limit'])  # 个人申购上限(万股)
    obj.funds = toFloat(row.loc['funds'])  # 募集资金(亿元)
    obj.ballot = toFloat(row.loc['ballot'])  # 网上中签率( %)
    return obj


class Model(Base):
    # 表的名字:
    __tablename__ = 'REF_NEW_STOCK'

    def __init__(self):
        pass

    # 表的结构:
    code = Column(String(32), primary_key=True)  # 代码
    name = Column(String(32))  # 名称
    date = Column(Date)  # 收集日期
    ipo_date = Column(Date, primary_key=True)  # 上网发行日期
    issue_date = Column(Date)  # 上市日期
    amount = Column(BigInteger)  # 发行数量(万股)
    markets = Column(BigInteger)  # 上网发行数量(万股)
    price = Column(Float(53))  # 发行价格(元)
    pe = Column(Float(53))  # 发行市盈率
    limit = Column(Float(53))  # 个人申购上限(万股)
    funds = Column(Float(53))  # 募集资金(亿元)
    ballot = Column(Float(53))  # 网上中签率( %)

