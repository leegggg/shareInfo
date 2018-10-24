from sqlalchemy import Column, Integer, Float, Date, String,DateTime
from share.model.dao import Base
from share.util.numberUtil import toFloat, toInt, dateTimeToTsStr
import logging
from datetime import datetime


def rowToORM(row, date: datetime):
    obj = Model()

    obj.date = date
    obj.avgPrice = toInt(row.loc['AvgPrice'])  # 平均票价
    obj.avpPeoPle = toInt(row.loc['AvpPeoPle'])  # 场均人次
    obj.boxOffice = toFloat(row.loc['BoxOffice'])  # 单日票房（万）
    obj.boxOffice_Up = toFloat(row.loc['BoxOffice_Up'])  # 环比变化 （ % ）
    obj.iRank = toInt(row.loc['IRank'])  # 排名
    obj.movieDay = toInt(row.loc['MovieDay'])  # 上映天数
    obj.movieName = str(row.loc['MovieName'])[0:Model.TEXT_MAX_LENGTH]  # 影片名
    obj.sumBoxOffice = toFloat(row.loc['SumBoxOffice'])  # 累计票房（万）
    obj.womIndex = toFloat(row.loc['WomIndex'])  # 口碑指数
    obj.pk = "{name}_{date}".format(name=obj.movieName,date=dateTimeToTsStr(date))

    return obj


class Model(Base):
    # 表的名字:
    __tablename__ = 'BOXOFFICE_DAY_BOXOFFICE'
    TEXT_MAX_LENGTH = 255

    def __init__(self):
        pass

    # 表的结构:
    pk = Column(String(265), primary_key=True)
    date = Column(Date)
    avgPrice = Column(Integer)  # 平均票价
    avpPeoPle = Column(Integer)  # 场均人次
    boxOffice = Column(Float(53))  # 单日票房（万）
    boxOffice_Up = Column(Float(53))  # 环比变化 （ % ）
    iRank = Column(Integer)  # 排名
    movieDay = Column(Integer)  # 上映天数
    movieName = Column(String(255))  # 影片名
    sumBoxOffice = Column(Float(53))  # 累计票房（万）
    womIndex = Column(Float(53))  # 口碑指数

