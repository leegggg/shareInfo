from sqlalchemy import Column, String, Float, Date
from share.model.dao import Base
from dateutil.parser import parse
import datetime

def rowToORM(row):
    obj = ClassifiedSt()
    obj.code = row.loc['code']
    obj.name = row.loc['name']
    obj.date = datetime.datetime.fromtimestamp(row.loc['date'].value / 1000000000)
    obj.weight = row.loc['weight']
    return obj


class ClassifiedSt(Base):
    # 表的名字:
    __tablename__ = 'CLASSIFIED_HS300S'

    def __init__(self):
        pass

    # 表的结构:
    code = Column(String(32), primary_key=True)  #  VDPP,
    name = Column(String(32))  #  observation,
    date = Column(Date, primary_key=True)
    weight = Column(Float)
