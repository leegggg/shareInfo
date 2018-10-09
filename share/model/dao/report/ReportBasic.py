from sqlalchemy import Column, String, Float, Date
from share.model.dao import Base
from datetime import datetime


def rowToORM(row,code):

    obj = Model()
    obj.code = code  # VDPP,
    obj.name = row.loc['name']  # observation,
    obj.industry = row.loc['industry']
    obj.area = row.loc['area']
    obj.pe = row.loc['pe']
    obj.outstanding = row.loc['outstanding']
    obj.totals = row.loc['totals']
    obj.totalAssets = row.loc['totalAssets']
    obj.liquidAssets = row.loc['liquidAssets']  # 流动资产
    obj.fixedAssets = row.loc['fixedAssets']  # 固定资产
    obj.reserved = row.loc['reserved']  # 公积金
    obj.reservedPerShare = row.loc['reservedPerShare']  # 每股公积金
    obj.esp = row.loc['esp']  # 每股收益
    obj.bvps = row.loc['bvps']  # 每股净资
    obj.pb = row.loc['pb']  # 市净率
    tsString = str(row.loc['timeToMarket'])   # 上市日期
    if len(tsString) < 8:
        obj.timeToMarket = None
    else:
        year, mon, day = int(tsString[:4]), int(tsString[4:6]), int(tsString[6:])
        datetime_object = datetime(year, mon, day)
        obj.timeToMarket = datetime_object
    obj.undp = row.loc['undp']  # 未分利润
    obj.perundp = row.loc['perundp']  # 每股未分配
    obj.rev = row.loc['rev']
    obj.profit = row.loc['profit']
    obj.gpr = row.loc['gpr']
    obj.npr = row.loc['npr']
    obj.holders = row.loc['holders']  # 股东人数
    return obj


# 定义User对象:
class Model(Base):
    # 表的名字:
    __tablename__ = 'REPORT_BASIC'

    # 表的结构:
    code = Column(String(32), primary_key=True)  # VDPP,
    name = Column(String(32))  # observation,
    industry = Column(String(32))
    area = Column(String(32))
    pe = Column(Float)
    outstanding = Column(Float)
    totals = Column(Float)
    totalAssets = Column(Float)
    liquidAssets = Column(Float)  # 流动资产
    fixedAssets = Column(Float)  # 固定资产
    reserved = Column(Float)  # 公积金
    reservedPerShare = Column(Float)  # 每股公积金
    esp = Column(Float)  # 每股收益
    bvps = Column(Float)  # 每股净资
    pb = Column(Float)  # 市净率
    timeToMarket = Column(Date)  # 上市日期
    undp = Column(Float)  # 未分利润
    perundp = Column(Float)  # 每股未分配
    rev = Column(Float)  # 收入同比( %)
    profit = Column(Float)  # 利润同比( %)
    gpr = Column(Float)  # 毛利率( %)
    npr = Column(Float)  # 净利润率( %)
    holders = Column(Float)  # 股东人数

