from sqlalchemy import Column, String, create_engine, Integer, Float, Text, Date
from sqlalchemy.orm import sessionmaker
from .TushareTableABS import TushareTableABS
from . import Base


def rowToORM(row):
    obj = FastReport(
        code=row.loc['code'], name=row.loc['name'], area=row.loc['area'])
    return obj


# 定义User对象:
class FastReport(Base):
    # 表的名字:
    __tablename__ = 'FAST_REPORT'

    # 表的结构:
    code = Column(String(32), primary_key=True)  #  VDPP,
    name = Column(String(32))  #  observation,
    eps = Column(Float)  #  946722600,
    eps_yoy = Column(Float)  #  946722600,
    bvps = Column(Float)  #  946722600,
    roe = Column(Float)  #  946722600,
    epcf = Column(Float)  #  946722600,
    net_profits = Column(Float)  #  946722600,
    profits_yoy = Column(Float)  #  946722600,
    distrib = Column(String(32))  #  946722600,
    report_date = Column(Date, primary_key=True)  #  946722600,
