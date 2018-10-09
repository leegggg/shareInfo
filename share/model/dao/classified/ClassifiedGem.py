from sqlalchemy import Column, String
from share.model.dao import Base


def rowToORM(row):
    obj = ClassifiedGem()
    obj.code = row.loc['code']
    obj.name = row.loc['name']
    return obj


class ClassifiedGem(Base):
    # 表的名字:
    __tablename__ = 'CLASSIFIED_GEM'

    def __init__(self):
        pass

    # 表的结构:
    code = Column(String(32), primary_key=True)  #  VDPP,
    name = Column(String(32))  #  observation,
