from sqlalchemy import Column, String, Float, Date
from share.model.dao import Base
from datetime import datetime
from dateutil.parser import parse
import logging
from share.util.numberUtil import toFloat

def rowToORM(row):
    obj = Model()
    tsString = str(row.loc['date'])
    obj.date = None
    try:
        obj.date = parse(tsString)
    except:
        logging.warning("Fail to get date from {} from {}. Using {} as Fallback".
                        format(__name__, tsString, obj.exe_date))

    obj.rON = toFloat(row.loc['ON'])  # 隔夜拆放利率
    obj.r1W = toFloat(row.loc['1W'])  # 1周拆放利率
    obj.r2W = toFloat(row.loc['2W'])  # 2周拆放利率
    obj.r1M = toFloat(row.loc['1M'])  # 1个月拆放利率
    obj.r3M = toFloat(row.loc['3M'])  # 3个月拆放利率
    obj.r6M = toFloat(row.loc['6M'])  # 6个月拆放利率
    obj.r9M = toFloat(row.loc['9M'])  # 9个月拆放利率
    obj.r1Y = toFloat(row.loc['1Y'])  # 1年拆放利率

    return obj


class Model(Base):
    # 表的名字:
    __tablename__ = 'SHIBOR_SHIBOR_DATA'
    TEXT_MAX_LENGTH = 255

    def __init__(self):
        pass

    # 表的结构:
    date = Column(Date, primary_key=True)  # 变动日期
    rON = Column(Float(53))  # 隔夜拆放利率
    r1W = Column(Float(53))  # 1周拆放利率
    r2W = Column(Float(53))  # 2周拆放利率
    r1M = Column(Float(53))  # 1个月拆放利率
    r3M = Column(Float(53))  # 3个月拆放利率
    r6M = Column(Float(53))  # 6个月拆放利率
    r9M = Column(Float(53))  # 9个月拆放利率
    r1Y = Column(Float(53))  # 1年拆放利率

