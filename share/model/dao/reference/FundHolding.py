from sqlalchemy import Column, Integer, Float, Date, String
from share.model.dao import Base
from share.util.numberUtil import toFloat, toInt
from dateutil.parser import parse
import logging


def rowToORM(row,year,quarter):
    obj = Model()

    obj.code = str(row.loc['code'])  # 股票代码
    obj.name = str(row.loc['name'])  # 股票名称

    obj.year = int(year)  # 分配年份
    obj.quarter = int(quarter)

    tsString = str(row.loc['date'])
    obj.report_date = None
    try:
        obj.report_date = parse(tsString)
    except:
        logging.warning("Fail to get date from {} from {}. Using {} as Fallback".
                        format(__name__, tsString, obj.report_date))

    obj.nums = toInt(row.loc['nums'])  # 基金家数
    obj.nlast = toInt(row.loc['nlast'])  # 与上期相比（增加或减少了）
    obj.count = toFloat(row.loc['count'])  # 基金持股数（万股）
    obj.clast = toFloat(row.loc['clast'])  # 与上期相比
    obj.amount = toFloat(row.loc['amount'])  # 基金持股市值
    obj.ratio = toFloat(row.loc['ratio'])  # 占流通盘比率
    return obj


class Model(Base):
    # 表的名字:
    __tablename__ = 'REF_FUND_HOLDING'

    def __init__(self):
        pass

    # 表的结构:
    code = Column(String(32), primary_key=True)  # 代码
    name = Column(String(32))  # 名称
    year = Column(Integer)
    quarter = Column(Integer)
    report_date = Column(Date, primary_key=True)  # 发布日期

    nums = Column(Integer)  # 基金家数
    nlast = Column(Integer)  # 与上期相比（增加或减少了）
    count = Column(Float)  # 基金持股数（万股）
    clast = Column(Float)  # 与上期相比
    amount = Column(Float)  # 基金持股市值
    ratio = Column(Float)  # 占流通盘比率

