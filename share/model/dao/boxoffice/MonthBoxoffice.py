from sqlalchemy import Column, Integer, Float, Date, String,DateTime
from share.model.dao import Base
from share.util.numberUtil import toFloat, toInt
from dateutil.parser import parse
import logging


def rowToORM(row, year, month):
    obj = Model()

    obj.year = year
    obj.month = month
    obj.avgPrice = toInt(row.loc['avgboxoffice'])  # 平均票价
    obj.avpPeoPle = toInt(row.loc['avgshowcount'])  # 场均人次
    obj.boxOffice = toFloat(row.loc['boxoffice'])  # 单日票房（万）
    obj.box_pro = toFloat(row.loc['box_pro'])  # 月度占比
    obj.iRank = toInt(row.loc['Irank'])  # 排名
    obj.movieName = str(row.loc['MovieName'])[0:Model.TEXT_MAX_LENGTH]  # 影片名

    if obj.movieName == "其他" or obj.movieName == "其它":
        return None

    obj.womIndex = toFloat(row.loc['WomIndex'])  # 口碑指数
    obj.days = toInt(row.loc['days'])
    tsString = str(row.loc['releaseTime'])
    obj.time = None
    try:
        obj.releaseTime = parse(tsString)
    except:
        logging.warning("Fail to get date from {} from {}. Using {} as Fallback".
                        format(__name__, tsString, obj.releaseTime))

    if obj.releaseTime is None:
        return None

    return obj


class Model(Base):
    # 表的名字:
    __tablename__ = 'BOXOFFICE_MONTH_BOXOFFICE'
    TEXT_MAX_LENGTH = 255

    def __init__(self):
        pass

    # 表的结构:
    year = Column(Integer, primary_key=True)
    month = Column(Integer, primary_key=True)
    avgPrice = Column(Integer)  # 平均票价
    avpPeoPle = Column(Integer)  # 场均人次
    boxOffice = Column(Float)  # 单日票房（万）
    box_pro = Column(Float)  # 月度占比
    iRank = Column(Integer)  # 排名
    movieName = Column(String(255), primary_key=True)  # 影片名
    womIndex = Column(Float)  # 口碑指数
    days = Column(Integer)
    releaseTime = Column(Date, primary_key=True)



