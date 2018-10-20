import tushare as ts
import logging
from share.model.dao import Base
from datetime import datetime
from datetime import timedelta

def updateRealtimeBoxoffice(con):
    import share.model.dao.boxoffice.RealtimeBoxoffice as Model
    logging.debug("Updating realtime boxoffice")
    df = ts.realtime_boxoffice(retry_count=16)
    res = []
    for _, row in df.iterrows():
        obj = Model.rowToORM(row)
        if obj is not None:
            res.append(obj)
    Base.metadata.create_all(con.engine)
    con.save_all(res)
    return


def updateDayBoxoffice(con, date: datetime):
    import share.model.dao.boxoffice.DayBoxoffice as Model
    dateString = date.strftime("%Y-%m-%d")
    logging.debug("Updating day boxoffice of {}".format(dateString))
    df = ts.day_boxoffice(date=dateString,retry_count=16)
    res = []
    for _, row in df.iterrows():
        obj = Model.rowToORM(row, date=date)
        if obj is not None:
            res.append(obj)
    Base.metadata.create_all(con.engine)
    con.save_all(res)
    return


def updateDayCinema(con, date: datetime):
    import share.model.dao.boxoffice.DayCinema as Model
    dateString = date.strftime("%Y-%m-%d")
    logging.debug("Updating day cinema of {}".format(dateString))
    df = ts.day_cinema(date=dateString,retry_count=16)
    res = []
    for _, row in df.iterrows():
        obj = Model.rowToORM(row, date=date)
        if obj is not None:
            res.append(obj)
    Base.metadata.create_all(con.engine)
    con.save_all(res)
    return


def updateMonthBoxoffice(con, year: int, month: int):
    import share.model.dao.boxoffice.MonthBoxoffice as Model
    dateString = "{year:04d}-{month:02d}".format(year=year,month=month)
    logging.debug("Updating month bboxoffice of {}".format(dateString))
    df = ts.month_boxoffice(date=dateString,retry_count=16)
    res = []
    for _, row in df.iterrows():
        obj = Model.rowToORM(row, year=year, month=month)
        if obj is not None:
            res.append(obj)
    Base.metadata.create_all(con.engine)
    con.save_all(res)
    return


def daily(con):
    logging.debug("Daily update boxOffice")
    date = datetime.now()
    updateDayBoxoffice(con=con, date=date)
    updateDayCinema(con=con, date=date)
    if date.day == 15:
        dateMonth = date - timedelta(days=20)
        updateMonthBoxoffice(con=con,year=dateMonth.year,month=dateMonth.month)

