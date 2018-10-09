from sqlalchemy import Column, String, Float, Date
from share.model.dao import Base
from dateutil.parser import parse

def rowToORM(row):
    obj = ClassifiedSt()
    obj.code = row.loc['code']
    obj.name = row.loc['name']
    obj.oDate = row.loc['oDate']
    obj.tDate = row.loc['tDate']
    return obj


class ClassifiedSt(Base):
    # 表的名字:
    __tablename__ = 'CLASSIFIED_TERMINATED'

    def __init__(self):
        pass

    # 表的结构:
    code = Column(String(32), primary_key=True)  #  VDPP,
    name = Column(String(32))  #  observation,
    oDate = Column(Date)
    tDate = Column(Date)
