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

    obj.ppiip = toFloat(row.loc['ppiip'])  # 工业品出厂价格指数
    obj.ppi = toFloat(row.loc['ppi'])  # 生产资料价格指数
    obj.qm = toFloat(row.loc['qm'])  # 采掘工业价格指数
    obj.rmi = toFloat(row.loc['rmi'])  # 原材料工业价格指数
    obj.pi = toFloat(row.loc['pi'])  # 加工工业价格指数
    obj.cg = toFloat(row.loc['cg'])  # 生活资料价格指数
    obj.food = toFloat(row.loc['food'])  # 食品类价格指数
    obj.clothing = toFloat(row.loc['clothing'])  # 衣着类价格指数
    obj.roeu = toFloat(row.loc['roeu'])  # 一般日用品价格指数
    obj.dcg = toFloat(row.loc['dcg'])  # 耐用消费品价格指数

    return obj


class Model(Base):
    # 表的名字:
    __tablename__ = 'MACRO_PPI'

    def __init__(self):
        pass

    # 表的结构:
    year = Column(Integer, primary_key=True)
    month = Column(Integer, primary_key=True)  # 统计时间
    ppiip = Column(Float)  # 工业品出厂价格指数
    ppi = Column(Float)  # 生产资料价格指数
    qm = Column(Float)  # 采掘工业价格指数
    rmi = Column(Float)  # 原材料工业价格指数
    pi = Column(Float)  # 加工工业价格指数
    cg = Column(Float)  # 生活资料价格指数
    food = Column(Float)  # 食品类价格指数
    clothing = Column(Float)  # 衣着类价格指数
    roeu = Column(Float)  # 一般日用品价格指数
    dcg = Column(Float)  # 耐用消费品价格指数


