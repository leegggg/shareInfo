from sqlalchemy import Column, Integer, Float, Date
from share.model.dao import Base
from share.util.numberUtil import toFloat
import logging

def rowToORM(row):
    obj = Model()

    obj.year = int(row.loc['year'])

    obj.end_for = toFloat(row.loc['end_for'])  # 最终消费支出贡献率( %)
    obj.for_rate = toFloat(row.loc['for_rate'])  # 最终消费支出拉动(百分点)
    obj.asset_for = toFloat(row.loc['asset_for'])  # 资本形成总额贡献率( %)
    obj.asset_rate = toFloat(row.loc['asset_rate'])  # 资本形成总额拉动(百分点)
    obj.goods_for = toFloat(row.loc['goods_for'])  # 货物和服务净出口贡献率( %)
    obj.goods_rate = toFloat(row.loc['goods_rate'])  # 货物和服务净出口拉动(百分点)

    return obj


class Model(Base):
    # 表的名字:
    __tablename__ = 'MACRO_GDP_FOR'

    def __init__(self):
        pass

    # 表的结构:
    year = Column(Integer, primary_key=True)
    end_for = Column(Float)  # 最终消费支出贡献率( %)
    for_rate = Column(Float)  # 最终消费支出拉动(百分点)
    asset_for = Column(Float)  # 资本形成总额贡献率( %)
    asset_rate = Column(Float)  # 资本形成总额拉动(百分点)
    goods_for = Column(Float)  # 货物和服务净出口贡献率( %)
    goods_rate = Column(Float)  # 货物和服务净出口拉动(百分点)


