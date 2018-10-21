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

    obj.rON_5 = toFloat(row.loc['ON_5'])  # 隔夜拆放利率
    obj.rON_10 = toFloat(row.loc['ON_10'])  # 隔夜拆放利率
    obj.rON_20 = toFloat(row.loc['ON_20'])  # 隔夜拆放利率

    obj.r1W_5 = toFloat(row.loc['1W_5'])  # 1周拆放利率
    obj.r1W_10 = toFloat(row.loc['1W_10'])  # 1周拆放利率
    obj.r1W_20 = toFloat(row.loc['1W_20'])  # 1周拆放利率

    obj.r2W_5 = toFloat(row.loc['2W_5'])  # 2周拆放利率
    obj.r2W_10 = toFloat(row.loc['2W_10'])  # 2周拆放利率

    return obj


class Model(Base):
    # 表的名字:
    __tablename__ = 'SHIBOR_SHIBOR_DATA'
    TEXT_MAX_LENGTH = 255

    def __init__(self):
        pass

    # 表的结构:
    date = Column(Date, primary_key=True)  # 变动日期
    rON_5 = Column(Float(53))  # 隔夜拆放利率
    rON_10 = Column(Float(53))  # 隔夜拆放利率
    rON_20 = Column(Float(53))  # 隔夜拆放利率

    r1W_5 = Column(Float(53))  # 1周拆放利率
    r1W_10 = Column(Float(53))  # 1周拆放利率
    r1W_20 = Column(Float(53))  # 1周拆放利率

    r2W_5 = Column(Float(53))  # 2周拆放利率
    r2W_10 = Column(Float(53))  # 2周拆放利率


