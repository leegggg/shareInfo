from sqlalchemy import Column, Integer, Float, Date
from share.model.dao import Base
from share.util.numberUtil import toFloat
import logging

def rowToORM(row):
    obj = Model()
    tsString = str(row.loc['month'])
    strs = tsString.split('.')
    if len(strs) < 2:
        obj.year = None
        obj.month = None
        logging.warning("Fail to get date from deposit rate. Using None as Fallback")
    else:
        obj.year = int(strs[0])
        obj.month = int(strs[1])

    obj.cpi = toFloat(row.loc['cpi'])  # cpi

    return obj


class Model(Base):
    # 表的名字:
    __tablename__ = 'MACRO_CPI'

    def __init__(self):
        pass

    # 表的结构:
    year = Column(Integer, primary_key=True)
    month = Column(Integer, primary_key=True)  # 统计时间
    cpi = Column(Float(53))  # CPI


