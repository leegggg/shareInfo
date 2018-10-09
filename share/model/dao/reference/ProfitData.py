from sqlalchemy import Column, Integer, Float, Date, String
from share.model.dao import Base
from share.util.numberUtil import toFloat
from dateutil.parser import parse
import logging

def rowToORM(row):
    obj = Model()

    obj.code = str(row.loc['code'])  # 股票代码
    obj.name = str(row.loc['name'])  # 股票名称
    obj.year = int(row.loc['year'])  # 分配年份

    tsString = str(row.loc['report_date'])
    obj.report_date = None
    try:
        obj.report_date = parse(tsString)
    except:
        logging.warning("Fail to get date from {} from {}. Using {} as Fallback".
                        format(__name__, tsString, obj.report_date))

    obj.divi = toFloat(row.loc['divi'])  # 分红金额（每10股）
    obj.shares = toFloat(row.loc['shares'])  # 转增和送股数（每10股）
    return obj


class Model(Base):
    # 表的名字:
    __tablename__ = 'REF_PROFIT_DATA'

    def __init__(self):
        pass

    # 表的结构:
    code = Column(String(32), primary_key=True)  # 股票代码
    name = Column(String(32))  # 股票名称
    year = Column(Integer)  # 分配年份
    report_date = Column(Date, primary_key=True)  # 公布日期
    divi = Column(Float)  # 分红金额（每10股）
    shares = Column(Float)  # 转增和送股数（每10股）

