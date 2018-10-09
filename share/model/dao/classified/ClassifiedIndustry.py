from sqlalchemy import Column, String
from share.model.dao import Base


def rowToORM(row):
    obj = ClassifiedIndustry()
    obj.code = row.loc['code']
    obj.name = row.loc['name']
    obj.c_name = row.loc['c_name']
    return obj


class ClassifiedIndustry(Base):
    # 表的名字:
    __tablename__ = 'CLASSIFIED_INDUSTRY'

    def __init__(self):
        pass

    # 表的结构:
    code = Column(String(32), primary_key=True)  #  VDPP,
    name = Column(String(32))  #  observation,
    c_name = Column(String(32), primary_key=True)  #  946722600,
