from sqlalchemy import Column, String, Float, Date
from share.model.dao import Base
from datetime import datetime
from dateutil.parser import parse
import logging
from share.util.numberUtil import toFloat, toStr

def rowToORM(row):
    obj = Model()
    tsString = str(row.loc['date'])
    obj.exe_date = None
    try:
        obj.exe_date = parse(tsString)
    except:
        logging.warning("Fail to get date from {} from {}. Using {} as Fallback".
                        format(__name__, tsString, obj.exe_date))

    obj.deposit_type = toStr(row.loc['deposit_type'][0:Model.TEXT_MAX_LENGTH])
    obj.rate = toFloat(row.loc['rate'])
    return obj


class Model(Base):
    # 表的名字:
    __tablename__ = 'MACRO_DEPOSIT_RATE'
    TEXT_MAX_LENGTH = 255

    def __init__(self):
        pass

    # 表的结构:
    exe_date = Column(Date, primary_key=True)  # 变动日期
    deposit_type = Column(String(255), primary_key=True)  # 存款种类
    rate = Column(Float(53))  # 利率（ % ）

