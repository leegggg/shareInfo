from sqlalchemy import Column, Integer, Float, Date
from share.model.dao import Base
from share.util.numberUtil import toFloat
import logging

def rowToORM(row):
    obj = Model()

    obj.year = int(row.loc['year'])

    obj.m2 = toFloat(row.loc['m2'])  # 货币和准货币(亿元)
    obj.m1 = toFloat(row.loc['m1'])  # 货币(亿元)
    obj.m0 = toFloat(row.loc['m0'])  # 流通中现金(亿元)
    obj.cd = toFloat(row.loc['cd'])  # 活期存款(亿元)
    obj.qm = toFloat(row.loc['qm'])  # 准货币(亿元)
    obj.ftd = toFloat(row.loc['ftd'])  # 定期存款(亿元)
    obj.sd = toFloat(row.loc['sd'])  # 储蓄存款(亿元)
    obj.rests = toFloat(row.loc['rests'])  # 其他存款(亿元)

    return obj


class Model(Base):
    # 表的名字:
    __tablename__ = 'MACRO_MONEY_SUPPLY_BAL'

    def __init__(self):
        pass

    # 表的结构:
    year = Column(Integer, primary_key=True)
    m2 = Column(Float)  # 货币和准货币(亿元)
    m1 = Column(Float)  # 货币(亿元)
    m0 = Column(Float)  # 流通中现金(亿元)
    cd = Column(Float)  # 活期存款(亿元)
    qm = Column(Float)  # 准货币(亿元)
    ftd = Column(Float)  # 定期存款(亿元)
    sd = Column(Float)  # 储蓄存款(亿元)
    rests = Column(Float)  # 其他存款(亿元)


