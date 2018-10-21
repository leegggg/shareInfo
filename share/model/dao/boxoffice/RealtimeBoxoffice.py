from sqlalchemy import Column, Integer, Float, Date, String,DateTime
from share.model.dao import Base
from share.util.numberUtil import toFloat, toInt
from dateutil.parser import parse
from datetime import datetime
import logging


def rowToORM(row):
    obj = Model()

    obj.boxOffice = toFloat(row.loc['BoxOffice'])  # 实时票房（万）
    obj.irank = toInt(row.loc['Irank'])  # 排名
    obj.movieName = str(row.loc['MovieName'])  # 影片名
    obj.boxPer = toFloat(row.loc['boxPer'])  # 票房占比 （ % ）
    obj.movieDay = toInt(row.loc['movieDay'])  # 上映天数
    obj.sumBoxOffice = toFloat(row.loc['sumBoxOffice'])  # 累计票房（万）

    tsString = str(row.loc['time'])
    obj.time = None
    try:
        obj.time = parse(tsString)
        minute = obj.time.minute
        if minute >= 30:
            minute = 30
        else:
            minute = 0
        tsString = obj.time.strftime("%Y-%m-%d %H")
        tsString = "{pre}:{min:02d}:00".format(pre=tsString,min=minute)
        obj.time = parse(tsString)
    except:
        logging.warning("Fail to get date from {} from {}. Using {} as Fallback".
                        format(__name__, tsString, obj.time))

    if obj.movieName == "其它":
        return None

    return obj


class Model(Base):
    # 表的名字:
    __tablename__ = 'BOXOFFICE_REALTIME_BOXOFFICE'
    TEXT_MAX_LENGTH = 255

    def __init__(self):
        pass

    # 表的结构:
    boxOffice = Column(Float(53))  # 实时票房（万）
    irank = Column(Integer)  # 排名
    movieName = Column(String(255), primary_key=True)  # 影片名
    boxPer = Column(Float(53))  # 票房占比 （ % ）
    movieDay = Column(Integer)  # 上映天数
    sumBoxOffice = Column(Float(53))  # 累计票房（万）
    time = Column(DateTime, primary_key=True)  # 数据获取时间

