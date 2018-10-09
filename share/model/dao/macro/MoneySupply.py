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

    obj.m2 = toFloat(row.loc['m2'])  # 货币和准货币（广义货币M2）(亿元)
    obj.m2_yoy = toFloat(row.loc['m2_yoy'])  # 货币和准货币（广义货币M2）同比增长( %)
    obj.m1 = toFloat(row.loc['m1'])  # 货币(狭义货币M1)(亿元)
    obj.m1_yoy = toFloat(row.loc['m1_yoy'])  # 货币(狭义货币M1)同比增长( %)
    obj.m0 = toFloat(row.loc['m0'])  # 流通中现金(M0)(亿元)
    obj.m0_yoy = toFloat(row.loc['m0_yoy'])  # 流通中现金(M0)同比增长( %)
    obj.cd = toFloat(row.loc['cd'])  # 活期存款(亿元)
    obj.cd_yoy = toFloat(row.loc['cd_yoy'])  # 活期存款同比增长( %)
    obj.qm = toFloat(row.loc['qm'])  # 准货币(亿元)
    obj.qm_yoy = toFloat(row.loc['qm_yoy'])  # 准货币同比增长( %)
    obj.ftd = toFloat(row.loc['ftd'])  # 定期存款(亿元)
    obj.ftd_yoy = toFloat(row.loc['ftd_yoy'])  # 定期存款同比增长( %)
    obj.sd = toFloat(row.loc['sd'])  # 储蓄存款(亿元)
    obj.sd_yoy = toFloat(row.loc['sd_yoy'])  # 储蓄存款同比增长( %)
    obj.rests = toFloat(row.loc['rests'])  # 其他存款(亿元)
    obj.rests_yoy = toFloat(row.loc['rests_yoy'])  # 其他存款同比增长( %)
    return obj


class Model(Base):
    # 表的名字:
    __tablename__ = 'MACRO_MONEY_SUPPLY'

    def __init__(self):
        pass

    # 表的结构:
    year = Column(Integer, primary_key=True)
    month = Column(Integer, primary_key=True)  # 统计时间
    m2 = Column(Float)  # 货币和准货币（广义货币M2）(亿元)
    m2_yoy = Column(Float)  # 货币和准货币（广义货币M2）同比增长( %)
    m1 = Column(Float)  # 货币(狭义货币M1)(亿元)
    m1_yoy = Column(Float)  # 货币(狭义货币M1)同比增长( %)
    m0 = Column(Float)  # 流通中现金(M0)(亿元)
    m0_yoy = Column(Float)  # 流通中现金(M0)同比增长( %)
    cd = Column(Float)  # 活期存款(亿元)
    cd_yoy = Column(Float)  # 活期存款同比增长( %)
    qm = Column(Float)  # 准货币(亿元)
    qm_yoy = Column(Float)  # 准货币同比增长( %)
    ftd = Column(Float)  # 定期存款(亿元)
    ftd_yoy = Column(Float)  # 定期存款同比增长( %)
    sd = Column(Float)  # 储蓄存款(亿元)
    sd_yoy = Column(Float)  # 储蓄存款同比增长( %)
    rests = Column(Float)  # 其他存款(亿元)
    rests_yoy = Column(Float)  # 其他存款同比增长( %)

