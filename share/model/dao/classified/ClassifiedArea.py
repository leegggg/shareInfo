from sqlalchemy import Column, String, create_engine, Integer, Float, Text, Date
from sqlalchemy.orm import sessionmaker
from share.model.dao import Base


def rowToORM(row):
    obj = ClassifiedArea()
    obj.code = str(row.loc['code'])
    obj.name = str(row.loc['name'])
    obj.area = row.loc['area']
    if obj.area != obj.area:
        obj.area = None
    return obj


class ClassifiedArea(Base):
    # 表的名字:
    __tablename__ = 'CLASSIFIED_AREA'

    def __init__(self):
        pass

    # 表的结构:
    code = Column(String(32), primary_key=True)  #  VDPP,
    name = Column(String(32))  #  observation,
    area = Column(String(32))  #  946722600,
