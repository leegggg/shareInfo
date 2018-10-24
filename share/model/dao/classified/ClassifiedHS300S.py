from sqlalchemy import Column, String, Float, Date
from share.model.dao import Base
from dateutil.parser import parse
from share.util.numberUtil import toFloat, dateTimeToTsStr
import datetime

def rowToORM(row):
    obj = ClassifiedSt()
    obj.code = row.loc['code']
    obj.name = row.loc['name']
    ts = datetime.datetime.fromtimestamp(row.loc['date'].value / 1000000000)
    obj.date = ts.date()
    obj.weight = toFloat(row.loc['weight'])
    # obj.pk = "{code}_{date}".format(code=obj.code,date=dateTimeToTsStr(ts))
    return obj


class ClassifiedSt(Base):
    # 表的名字:
    __tablename__ = 'CLASSIFIED_HS300S'

    def __init__(self):
        pass

    # 表的结构:
    # pk = Column(String(40), primary_key=True)
    code = Column(String(32), primary_key=True)  #  VDPP,
    name = Column(String(32))  #  observation,
    date = Column(Date, primary_key=True)
    weight = Column(Float)
