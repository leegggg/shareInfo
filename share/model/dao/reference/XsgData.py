from sqlalchemy import Column, Integer, Float, Date, String
from share.model.dao import Base
from share.util.numberUtil import toFloat, toStr
from dateutil.parser import parse
import logging


def rowToORM(row, year, month):
    obj = Model()

    obj.code = toStr(row.loc['code'])  # 股票代码
    obj.name = toStr(row.loc['name'])  # 股票名称

    obj.year = int(year)  # 分配年份
    obj.month = int(month)

    tsString = toStr(row.loc['date'])
    obj.report_date = None
    try:
        obj.report_date = parse(tsString)
    except:
        logging.warning("Fail to get date from {} from {}. Using {} as Fallback".
                        format(__name__, tsString, obj.report_date))

    obj.count = toFloat(row.loc['count'])
    obj.ratio = toFloat(row.loc['ratio'])
    return obj


class Model(Base):
    # 表的名字:
    __tablename__ = 'REF_XSG_DATA'

    def __init__(self):
        pass

    # 表的结构:
    code = Column(String(32), primary_key=True)  # 代码
    name = Column(String(32))  # 名称
    year = Column(Integer)
    month = Column(Integer)
    report_date = Column(Date, primary_key=True)  # 发布日期
    count = Column(Float(53))  # 解禁数量（万股）
    ratio = Column(Float(53))  # 占总盘比率%

