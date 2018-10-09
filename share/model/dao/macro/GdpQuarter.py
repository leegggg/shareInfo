from sqlalchemy import Column, Integer, Float, Date
from share.model.dao import Base
from share.util.numberUtil import toFloat
import logging

def rowToORM(row):
    obj = Model()
    tsString = str(row.loc['quarter'])
    strs = tsString.split('.')
    if len(strs) < 2:
        obj.year = None
        obj.quarter = None
        logging.warning("Fail to get date from deposit rate. Using None as Fallback")
    else:
        obj.year = int(strs[0])
        obj.quarter = int(strs[1])

    obj.gdp_yoy = toFloat(row.loc['gdp_yoy'])  # 国内生产总值同比增长( %)
    obj.pi = toFloat(row.loc['pi'])  # 第一产业增加值(亿元)
    obj.pi_yoy = toFloat(row.loc['pi_yoy'])  # 第一产业增加值同比增长( %)
    obj.si = toFloat(row.loc['si'])  # 第二产业增加值(亿元)
    obj.si_yoy = toFloat(row.loc['si_yoy'])  # 第二产业增加值同比增长( %)
    obj.ti = toFloat(row.loc['ti'])  # 第三产业增加值(亿元)
    obj.ti_yoy = toFloat(row.loc['ti_yoy'])  # 第三产业增加值同比增长( %)
    return obj


class Model(Base):
    # 表的名字:
    __tablename__ = 'MACRO_GDP_QUARTER'

    def __init__(self):
        pass

    # 表的结构:
    year = Column(Integer, primary_key=True)
    quarter = Column(Integer, primary_key=True)  # 统计时间
    gdp_yoy = Column(Float)  # 国内生产总值同比增长( %)
    pi = Column(Float)  # 第一产业增加值(亿元)
    pi_yoy = Column(Float)  # 第一产业增加值同比增长( %)
    si = Column(Float)  # 第二产业增加值(亿元)
    si_yoy = Column(Float)  # 第二产业增加值同比增长( %)
    ti = Column(Float)  # 第三产业增加值(亿元)
    ti_yoy = Column(Float)  # 第三产业增加值同比增长( %)

