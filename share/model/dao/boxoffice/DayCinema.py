from sqlalchemy import Column, Integer, Float, Date, String,DateTime
from share.model.dao import Base
from share.util.numberUtil import toFloat, toInt, dateTimeToTsStr
from dateutil.parser import parse
from datetime import datetime
import logging


def rowToORM(row, date:datetime):
    obj = Model()

    obj.attendance = toFloat(row.loc['Attendance'])  # 上座率
    obj.avgPeople = toFloat(row.loc['AvgPeople'])  # 场均人次
    obj.cinemaName = str(row.loc['CinemaName'])[0:Model.TEXT_MAX_LENGTH]  # 影院名称
    obj.iRank = toFloat(row.loc['RowNum'])  # 排名
    obj.todayAudienceCount = toFloat(row.loc['TodayAudienceCount'])  # 当日观众人数
    obj.todayBox = toFloat(row.loc['TodayBox'])  # 当日票房
    obj.todayShowCount = toFloat(row.loc['TodayShowCount'])  # 当日场次
    obj.price = toFloat(row.loc['price'])  # 场均票价（元）
    obj.pk = "{name}_{date}".format(name=obj.cinemaName, date=dateTimeToTsStr(date))

    obj.date = date

    return obj


class Model(Base):
    # 表的名字:
    __tablename__ = 'BOXOFFICE_DAY_CINEMA'
    TEXT_MAX_LENGTH = 255

    def __init__(self):
        pass

    # 表的结构:
    pk = Column(String(265), primary_key=True)
    date = Column(Date)
    attendance = Column(Float(53))  # 上座率
    avgPeople = Column(Float(53))  # 场均人次
    cinemaName = Column(String(255))  # 影院名称
    iRank = Column(Integer)  # 排名
    todayAudienceCount = Column(Integer)  # 当日观众人数
    todayBox = Column(Float(53))  # 当日票房
    todayShowCount = Column(Float(53))  # 当日场次
    price = Column(Float(53))  # 场均票价（元）



