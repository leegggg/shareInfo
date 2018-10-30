from sqlalchemy import Column, String, Float, Date
from share.model.dao import Base
from datetime import datetime
from share.util.numberUtil import toFloat, toStr


def rowToORM(row,code):

    obj = Model()
    obj.code = code  # VDPP,
    obj.name = toStr(row.loc['name'])  # observation,
    obj.industry = toStr(row.loc['industry'])
    obj.area = toStr(row.loc['area'])
    obj.pe = toFloat(row.loc['pe'])
    obj.outstanding = toFloat(row.loc['outstanding'])
    obj.totals = toFloat(row.loc['totals'])
    obj.totalAssets = toFloat(row.loc['totalAssets'])
    obj.liquidAssets = toFloat(row.loc['liquidAssets'])  # 流动资产
    obj.fixedAssets = toFloat(row.loc['fixedAssets'])  # 固定资产
    obj.reserved = toFloat(row.loc['reserved'])  # 公积金
    obj.reservedPerShare = toFloat(row.loc['reservedPerShare'])  # 每股公积金
    obj.esp = toFloat(row.loc['esp'])  # 每股收益
    obj.bvps = toFloat(row.loc['bvps'])  # 每股净资
    obj.pb = toFloat(row.loc['pb'])  # 市净率
    tsString = str(row.loc['timeToMarket'])   # 上市日期
    if len(tsString) < 8:
        obj.timeToMarket = None
    else:
        year, mon, day = int(tsString[:4]), int(tsString[4:6]), int(tsString[6:])
        datetime_object = datetime(year, mon, day)
        obj.timeToMarket = datetime_object
    obj.undp = toFloat(row.loc['undp'])  # 未分利润
    obj.perundp = toFloat(row.loc['perundp'])  # 每股未分配
    obj.rev = toFloat(row.loc['rev'])
    obj.profit = toFloat(row.loc['profit'])
    obj.gpr = toFloat(row.loc['gpr'])
    obj.npr = toFloat(row.loc['npr'])
    obj.holders = toFloat(row.loc['holders'])  # 股东人数
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
    pe = Column(Float(53))
    outstanding = Column(Float(53))
    totals = Column(Float(53))
    totalAssets = Column(Float(53))
    liquidAssets = Column(Float(53))  # 流动资产
    fixedAssets = Column(Float(53))  # 固定资产
    reserved = Column(Float(53))  # 公积金
    reservedPerShare = Column(Float(53))  # 每股公积金
    esp = Column(Float(53))  # 每股收益
    bvps = Column(Float(53))  # 每股净资
    pb = Column(Float(53))  # 市净率
    timeToMarket = Column(Date)  # 上市日期
    undp = Column(Float(53))  # 未分利润
    perundp = Column(Float(53))  # 每股未分配
    rev = Column(Float(53))  # 收入同比( %)
    profit = Column(Float(53))  # 利润同比( %)
    gpr = Column(Float(53))  # 毛利率( %)
    npr = Column(Float(53))  # 净利润率( %)
    holders = Column(Float(53))  # 股东人数

