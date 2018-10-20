import tushare as ts
import logging
from share.model.dao import Base
from datetime import datetime


def updaterPofitData(con, year: int=None,top: int=10000):
    import share.model.dao.reference.ProfitData as Model
    if year is None:
        year = datetime.now().year

    logging.debug("Updating PofitData of year {} top {}".format(year,top))
    df = ts.profit_data(year=year,top=top,retry_count=16)
    res = []
    for _, row in df.iterrows():
        obj = Model.rowToORM(row)
        if obj is not None:
            res.append(obj)
    Base.metadata.create_all(con.engine)
    con.save_all(res)
    return


def updateForecastDate(con, year: int, quarter: int):
    import share.model.dao.reference.ForecastData as Model
    logging.debug("Updating day updateForecastDate of {}Q{}".format(year,quarter))
    df = ts.forecast_data(year,quarter)
    res = []
    for _, row in df.iterrows():
        obj = Model.rowToORM(row,year=year,quarter=quarter)
        if obj is not None:
            res.append(obj)
    Base.metadata.create_all(con.engine)
    con.save_all(res)
    return


def updateXsgData(con, year: int, month: int):
    import share.model.dao.reference.XsgData as Model
    dateString = "{year:04d}-{month:02d}".format(year=year,month=month)
    logging.debug("Updating month XsgData of {}".format(dateString))
    df = ts.xsg_data(year=year,month=month,retry_count=16)
    res = []
    for _, row in df.iterrows():
        obj = Model.rowToORM(row, year=year, month=month)
        if obj is not None:
            res.append(obj)
    Base.metadata.create_all(con.engine)
    con.save_all(res)
    return


def updateFundHoldings(con, year: int, quarter: int, retry_count: int=4):
    import share.model.dao.reference.FundHolding as Model
    logging.debug("Updating day updateFundHoldings of {}Q{}".format(year,quarter))
    df = ts.fund_holdings(year,quarter,retry_count=retry_count)
    res = []
    for _, row in df.iterrows():
        obj = Model.rowToORM(row,year=year,quarter=quarter)
        if obj is not None:
            res.append(obj)
    Base.metadata.create_all(con.engine)
    con.save_all(res)
    return


def updateNewStocks(con):
    from share.service.basicInfoService import getBasicInfo
    import share.model.dao.reference.NewStock as package
    getBasicInfo(con=con,package=package,fun=ts.new_stocks,clean=False)
    return


def updateMarginsSZ(con,start: datetime=None, end : datetime=None):
    import share.model.dao.reference.MarginSZ as Model
    dateFormat = "%Y-%m-%d"
    if start is None:
        start = datetime.now()
    if end is None:
        end = datetime.now()

    logging.debug("Updating MarginsSZ from {start} to {end}".
                  format(start=start.strftime(dateFormat),end=end.strftime(dateFormat)))

    df = ts.sz_margins(start=start.strftime(dateFormat),end=end.strftime(dateFormat),retry_count=32)

    res = []
    for _, row in df.iterrows():
        obj = Model.rowToORM(row)
        if obj is not None:
            res.append(obj)
    Base.metadata.create_all(con.engine)
    con.save_all(res)
    return


def updateMarginDetailSZ(con,date: datetime=None, retry_count: int=4):
    import share.model.dao.reference.MarginDetailSZ as Model
    dateFormat = "%Y-%m-%d"
    if date is None:
        date = datetime.now()

    logging.debug("Updating MarginsSZ detail of {date}".
                  format(date=date.strftime(dateFormat)))

    df = ts.sz_margin_details(date=date.strftime(dateFormat),retry_count=retry_count)

    res = []
    for _, row in df.iterrows():
        obj = Model.rowToORM(row)
        if obj is not None:
            res.append(obj)
    Base.metadata.create_all(con.engine)
    con.save_all(res)
    return


def getAll(con, start: datetime, end: datetime):
    from share.util.dateModel import YearQuarter
    from datetime import timedelta

    logging.debug("Daily update for reference")

    date = start
    while date.timestamp() < end.timestamp():
        # daily
        try:
            updateMarginDetailSZ(con=con, date=date)
        except:
            logging.warning("Failed to get update MarginDetailSZ {}".format(str(date)))
            pass

        if date.day == 15:
            # Monthly
            try:
                updateMarginsSZ(con=con, start=date - timedelta(days=45),end=date)
            except:
                logging.warning("Failed to get update updateMarginsSZ {} - {}".format(
                    str(date - timedelta(days=45)),str(date)))

            try:
                updateXsgData(con=con, year=date.year, month=date.month)
            except:
                logging.warning("Failed to get update updateXsgData {}.{}".format(
                    str(date.year),str(date.month)))

            # Quarterly
            if date.month % 4 == 1:
                try:
                    updaterPofitData(con=con,year=date.year)
                except:
                    logging.warning("Failed to get update updaterPofitData {}".format(str(date.year)))

                lastYearQuarter = YearQuarter.fromDate(date)
                try:
                    updateForecastDate(con=con,year=lastYearQuarter.year,quarter=lastYearQuarter.quarter)
                except OSError:
                    logging.warning("Failed to get updateForecastDate {} try last quarter".format(str(lastYearQuarter)))

                try:
                    updateFundHoldings(con=con,year=lastYearQuarter.year,quarter=lastYearQuarter.quarter)
                except OSError:
                    logging.warning("Failed to get updateFundHoldings {} try last quarter".format(str(lastYearQuarter)))
        date = date + timedelta(days=1)
    return


def daily(con):
    from share.util.dateModel import YearQuarter
    from datetime import timedelta

    logging.debug("Daily update for reference")

    dateNow = datetime.now()
    lastYearQuarter = YearQuarter.fromDate(dateNow).__last__()

    try:
        updateForecastDate(con=con,year=lastYearQuarter.year,quarter=lastYearQuarter.quarter)
    except OSError:
        logging.warning("Failed to get updateForecastDate {} try last quarter".format(str(lastYearQuarter)))
        lastYearQuarter = lastYearQuarter.__last__()
        try:
            updateForecastDate(con=con,year=lastYearQuarter.year,quarter=lastYearQuarter.quarter)
        except OSError:
            logging.warning("Failed to get updateForecastDate {} give up".format(str(lastYearQuarter)))

    try:
        updateFundHoldings(con=con,year=lastYearQuarter.year,quarter=lastYearQuarter.quarter)
    except OSError:
        logging.warning("Failed to get updateFundHoldings {} try last quarter".format(str(lastYearQuarter)))
        lastYearQuarter = lastYearQuarter.__last__()
        try:
            updateFundHoldings(con=con,year=lastYearQuarter.year,quarter=lastYearQuarter.quarter)
        except OSError:
            logging.warning("Failed to get updateFundHoldings {} give up".format(str(lastYearQuarter)))

    try:
        updateMarginDetailSZ(con=con)
    except OSError:
        logging.warning("Failed to get update MarginDetailSZ {}".format(str(dateNow)))
        pass

    try:
        updateMarginDetailSZ(con=con,date=dateNow - timedelta(days=1))
    except OSError:
        logging.warning("Failed to update MarginDetailSZ {}".format(str(dateNow - timedelta(days=1))))
        pass

    updateMarginsSZ(con=con,start=dateNow - timedelta(days=7))

    updateNewStocks(con=con)

    updaterPofitData(con=con)

    updateXsgData(con=con, year=dateNow.year, month=dateNow.month)

    lastMonth = dateNow - timedelta(days=28)

    updateXsgData(con=con,year=lastMonth.year,month=lastMonth.month)

    return