import logging
from share.util.dateModel import YearQuarter
from datetime import datetime
from datetime import timedelta
from influxdb import InfluxDBClient
from multiprocessing import Queue
import logging
import tushare as ts
from share.model.dao import tick
from share.client import influxClient


def saveTicks(points, dbinfo: dict):
    client = influxClient.getClient(dbinfo=dbinfo)
    client.write_points(points=points, database='shareDev')
    return


def downloadTicks(code: str, date: datetime, dbinfo: dict, source='tt') -> [dict]:
    dateStr = date.strftime("%Y-%m-%d")
    logging.info("Downloading ticks code: {}, date: {}".format(code, dateStr))
    ticks = ts.get_tick_data(code=code, date=dateStr, src=source)
    points = []

    if ticks is None:
        logging.info("Skip {} at {} as ticks is None".format(code, dateStr))
        return points

    for _, row in ticks.iterrows():
        points.append(tick.rowToORM(row=row, code=code, currentStr=dateStr))

    logging.info("Saving ticks code: {}, date: {}".format(code, dateStr))
    saveTicks(points=points, dbinfo=dbinfo)
    return points


def getTickAsync(codes, dbinfo:dict, start=None, end=None, multiplier: int = 2):
    import multiprocessing
    from multiprocessing import pool

    if end is None:
        end = datetime.now()

    threads = multiplier * multiprocessing.cpu_count()

    logging.debug("getTicksAsync length: {}, end: {}, start: {} with {} processes".format(
        len(codes), end.strftime("%Y-%m-%d"), start.strftime("%Y-%m-%d"), threads))

    workerPool = pool.Pool(threads)

    # Download data to MQ
    current = start
    while current < end:
        # Weekends
        if current.weekday() >= 5:
            current = current + timedelta(days=1)
            continue

        for code in codes:
            kwds = {
                'code': code,
                'date': current,
                'dbinfo': dbinfo
            }
            workerPool.apply_async(func=downloadTicks, kwds=kwds, error_callback=logging.warning)

        current = current + timedelta(days=1)

    workerPool.close()
    # Download finished
    workerPool.join()

    return
