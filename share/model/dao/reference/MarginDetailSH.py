from sqlalchemy import Column, Integer, Float, Date, String
from share.model.dao import Base
from share.util.numberUtil import toFloat, toInt
from dateutil.parser import parse
import logging


def rowToORM(row):
    obj = Model()

    obj.code = str(row.loc['stockCode'])  # 标的证券代码
    obj.name = str(row.loc['securityAbbr'])  # 标的证券简称

    tsString = str(row.loc['opDate'])
    obj.opDate = None
    try:
        obj.opDate = parse(tsString)
    except:
        logging.warning("Fail to get date from {} from {}. Using {} as Fallback".
                        format(__name__, tsString, obj.opDate))

    obj.rzye = toInt(row.loc['rzye'])  # 本日融资余额(元)
    obj.rzmre = toInt(row.loc['rzmre'])  # 本日融资买入额(元)
    obj.rzche = toInt(row.loc['rzche'])  # 本日融资偿还额(元)
    obj.rqyl = toInt(row.loc['rqyl'])  # 本日融券余量
    obj.rqmcl = toInt(row.loc['rqmcl'])  # 本日融券卖出量
    obj.rqchl = toInt(row.loc['rqchl'])  # 本日融券偿还量

    return obj


class Model(Base):
    # 表的名字:
    __tablename__ = 'REF_MARGIN_DETAIL_SH'

    def __init__(self):
        pass

    # 表的结构:
    opDate = Column(Date, primary_key=True)  # 信用交易日期
    code = Column(String(32), primary_key=True)  # 标的证券代码
    name = Column(String(32))  # 标的证券简称
    rzye = Column(Integer)  # 本日融资余额(元)
    rzmre = Column(Integer)  # 本日融资买入额(元)
    rzche = Column(Integer)  # 本日融资偿还额(元)
    rqyl = Column(Integer)  # 本日融券余量
    rqmcl = Column(Integer)  # 本日融券卖出量
    rqchl = Column(Integer)  # 本日融券偿还量


