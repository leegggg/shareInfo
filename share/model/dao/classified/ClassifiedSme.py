from sqlalchemy import Column, String
from share.model.dao import Base
from share.util.numberUtil import toStr


def rowToORM(row):
    obj = ClassifiedSme()
    obj.code = toStr(row.loc['code'])
    obj.name = toStr(row.loc['name'])
    return obj


class ClassifiedSme(Base):
    # 表的名字:
    __tablename__ = 'CLASSIFIED_SME'

    def __init__(self):
        pass

    # 表的结构:
    code = Column(String(32), primary_key=True)  #  VDPP,
    name = Column(String(32))  #  observation,
