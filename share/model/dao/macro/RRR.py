from sqlalchemy import Column, String, Float, Date
from share.model.dao import Base
from datetime import datetime
from share.util.numberUtil import toFloat
from dateutil.parser import parse
import logging

def rowToORM(row):
    obj = Model()
    tsString = str(row.loc['date'])
    obj.exe_date = None
    try:
        obj.exe_date = parse(tsString)
    except:
        logging.warning("Fail to get date from {} from {}. Using {} as Fallback".
                        format(__name__, tsString, obj.exe_date))

    obj.before = toFloat(row.loc['before'])
    obj.now = toFloat(row.loc['now'])
    obj.changed = toFloat(row.loc['changed'])
    return obj


class Model(Base):
    # 表的名字:
    # 存款准备金率
    __tablename__ = 'MACRO_RRR'
    TEXT_MAX_LENGTH = 255

    def __init__(self):
        pass




    # 表的结构:
    exe_date = Column(Date, primary_key=True)  # 变动日期
    before = Column(Float(53))  # before: 调整前存款准备金率( %)
    now = Column(Float(53))  # now: 调整后存款准备金率( %)
    changed = Column(Float(53))  # changed: 调整幅度( %)

