from sqlalchemy import Column, Integer, Float, Date, String
from share.model.dao import Base
from share.util.numberUtil import toFloat
from dateutil.parser import parse
import logging

def rowToORM(row,year,quarter):
    obj = Model()

    obj.code = str(row.loc['code'])  # 股票代码
    obj.name = str(row.loc['name'])  # 股票名称
    obj.type = str(row.loc['type'])

    obj.year = int(year)  # 分配年份
    obj.quarter = int(quarter)

    tsString = str(row.loc['report_date'])
    obj.report_date = None
    try:
        obj.report_date = parse(tsString)
    except:
        logging.warning("Fail to get date from {} from {}. Using {} as Fallback".
                        format(__name__, tsString, obj.report_date))

    obj.pre_eps = toFloat(row.loc['pre_eps'])  # 分红金额（每10股）
    obj.range = str(row.loc['range'])[0:255]  # 转增和送股数（每10股）
    return obj


class Model(Base):
    # 表的名字:
    __tablename__ = 'REF_FORECAST_DATA'

    def __init__(self):
        pass

    # 表的结构:
    code = Column(String(32), primary_key=True)  # 代码
    name = Column(String(32))  # 名称
    type = Column(String(32))  # 业绩变动类型【预增、预亏等】
    year = Column(Integer)
    quarter = Column(Integer)
    report_date = Column(Date, primary_key=True)  # 发布日期
    pre_eps = Column(Float(53))  # 上年同期每股收益
    range = Column(String(255))  # 业绩变动范围

