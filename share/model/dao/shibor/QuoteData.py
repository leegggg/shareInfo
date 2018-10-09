from sqlalchemy import Column, String, Float, Date
from share.model.dao import Base
from datetime import datetime
from dateutil.parser import parse
import logging
from share.util.numberUtil import toFloat

def rowToORM(row):
    obj = Model()
    tsString = str(row.loc['date'])
    obj.date = None
    try:
        obj.date = parse(tsString)
    except:
        logging.warning("Fail to get date from {} from {}. Using {} as Fallback".
                        format(__name__, tsString, obj.exe_date))

    obj.bank = str(row.loc['bank'])

    obj.rON = toFloat(row.loc['ON'])  # 隔夜拆放利率
    obj.rON_B = toFloat(row.loc['ON_B'])  # 隔夜拆放买入价
    obj.rON_A = toFloat(row.loc['ON_A'])  # 隔夜拆放卖出价
    obj.r1W_B = toFloat(row.loc['1W_B'])  # 1周买入
    obj.r1W_A = toFloat(row.loc['1W_A'])  # 1周卖出
    obj.r2W_B = toFloat(row.loc['2W_B'])  # 买入
    obj.r2W_A = toFloat(row.loc['2W_A'])  # 卖出
    obj.r1M_B = toFloat(row.loc['1M_B'])  # 买入
    obj.r1M_A = toFloat(row.loc['1M_A'])  # 卖出
    obj.r3M_B = toFloat(row.loc['3M_B'])  # 买入
    obj.r3M_A = toFloat(row.loc['3M_A'])  # 卖出
    obj.r6M_B = toFloat(row.loc['6M_B'])  # 买入
    obj.r6M_A = toFloat(row.loc['6M_A'])  # 卖出
    obj.r9M_B = toFloat(row.loc['9M_B'])  # 买入
    obj.r9M_A = toFloat(row.loc['9M_A'])  # 卖出
    obj.r1Y_B = toFloat(row.loc['1Y_B'])  # 买入
    obj.r1Y_A = toFloat(row.loc['1Y_A'])  # 卖出


    return obj


class Model(Base):
    # 表的名字:
    __tablename__ = 'SHIBOR_QUOTE_DATA'
    TEXT_MAX_LENGTH = 255

    def __init__(self):
        pass

    # 表的结构:
    date = Column(Date, primary_key=True)  # 变动日期
    bank = Column(String(64), primary_key=True)  # 报价银行名称
    rON = Column(Float)  # 隔夜拆放利率
    rON_B = Column(Float)  # 隔夜拆放买入价
    rON_A = Column(Float)  # 隔夜拆放卖出价
    r1W_B = Column(Float)  # 1周买入
    r1W_A = Column(Float)  # 1周卖出
    r2W_B = Column(Float)  # 买入
    r2W_A = Column(Float)  # 卖出
    r1M_B = Column(Float)  # 买入
    r1M_A = Column(Float)  # 卖出
    r3M_B = Column(Float)  # 买入
    r3M_A = Column(Float)  # 卖出
    r6M_B = Column(Float)  # 买入
    r6M_A = Column(Float)  # 卖出
    r9M_B = Column(Float)  # 买入
    r9M_A = Column(Float)  # 卖出
    r1Y_B = Column(Float)  # 买入
    r1Y_A = Column(Float)  # 卖出

