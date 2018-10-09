from sqlalchemy import Column, Integer, Float, Date
from share.model.dao import Base
from share.util.numberUtil import toFloat
import logging

def rowToORM(row):
    obj = Model()

    obj.year = int(row.loc['year'])

    obj.gdp = toFloat(row.loc['gdp'])  # 国内生产总值(亿元)
    obj.pc_gdp = toFloat(row.loc['pc_gdp'])  # 人均国内生产总值(元)
    obj.gnp = toFloat(row.loc['gnp'])  # 国民生产总值(亿元)
    obj.pi = toFloat(row.loc['pi'])  # 第一产业(亿元)
    obj.si = toFloat(row.loc['si'])  # 第二产业(亿元)
    obj.industry = toFloat(row.loc['industry'])  # 工业(亿元)
    obj.cons_industry = toFloat(row.loc['cons_industry'])  # 建筑业(亿元)
    obj.ti = toFloat(row.loc['ti'])  # 第三产业(亿元)
    obj.trans_industry = toFloat(row.loc['trans_industry'])  # 交通运输仓储邮电通信业(亿元)
    obj.lbdy = toFloat(row.loc['lbdy'])  # 批发零售贸易及餐饮业(亿元)

    return obj


class Model(Base):
    # 表的名字:
    __tablename__ = 'MACRO_GDP_YEAR'

    def __init__(self):
        pass

    # 表的结构:
    year = Column(Integer, primary_key=True)
    gdp = Column(Float)  # 国内生产总值(亿元)
    pc_gdp = Column(Float)  # 人均国内生产总值(元)
    gnp = Column(Float)  # 国民生产总值(亿元)
    pi = Column(Float)  # 第一产业(亿元)
    si = Column(Float)  # 第二产业(亿元)
    industry = Column(Float)  # 工业(亿元)
    cons_industry = Column(Float)  # 建筑业(亿元)
    ti = Column(Float)  # 第三产业(亿元)
    trans_industry = Column(Float)  # 交通运输仓储邮电通信业(亿元)
    lbdy = Column(Float)  # 批发零售贸易及餐饮业(亿元)


