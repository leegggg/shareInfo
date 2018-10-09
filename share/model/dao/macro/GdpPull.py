from sqlalchemy import Column, Integer, Float, Date
from share.model.dao import Base
from share.util.numberUtil import toFloat
import logging

def rowToORM(row):
    obj = Model()

    obj.year = int(row.loc['year'])

    obj.gdp_yoy = toFloat(row.loc['gdp_yoy'])  # 国内生产总值同比增长( %)
    obj.pi = toFloat(row.loc['pi'])  # 第一产业拉动率( %)
    obj.si = toFloat(row.loc['si'])  # 第二产业拉动率( %)
    obj.industry = toFloat(row.loc['industry'])  # 其中工业拉动( %)
    obj.ti = toFloat(row.loc['ti'])  # 第三产业拉动率( %)

    return obj


class Model(Base):
    # 表的名字:
    __tablename__ = 'MACRO_GDP_PULL'

    def __init__(self):
        pass

    # 表的结构:
    year = Column(Integer, primary_key=True)
    gdp_yoy = Column(Float)  # 国内生产总值同比增长( %)
    pi = Column(Float)  # 第一产业拉动率( %)
    si = Column(Float)  # 第二产业拉动率( %)
    industry = Column(Float)  # 其中工业拉动( %)
    ti = Column(Float)  # 第三产业拉动率( %)


