import logging
from multiprocessing import Queue
import tushare as ts
from datetime import datetime
from datetime import timedelta
from share.model.dao import Base


def updateKline(code, con, ktype='D', start=None):
    from share.model.dao import KLine

    if start is None:
        start = datetime.now() - timedelta(days=90)
    start = start.strftime('%Y-%m-%d')

    logging.debug("Kline of [{}] type {} from {}".format(code, ktype ,start))
    klines = ts.get_k_data(code=code, ktype=ktype, start=start)
    res = []
    for _, row in klines.iterrows():
        res.append(KLine.rowToORM(row, "k_{}".format(code, ktype), ktype=ktype))
    Base.metadata.create_all(con.engine)
    con.save_all(res, oneByOne=True)
    return


def getKLines(dbClient, codes, ktype='D', start=None):
    if start is None:
        start = datetime.now() - timedelta(days=90)

    for code in codes:
        updateKline(code, dbClient, ktype, start)
    return


def downloadKlineToQueue(q: Queue, code: str, ktype: str='D', index: bool=False, start=None):
    if start is None:
        start = datetime.now() - timedelta(days=90)
    start = start.strftime('%Y-%m-%d')
    logging.debug("Downloading Kline of [{}] type {} from {} in MQ {}".format(code, ktype, start, q.qsize()))
    klines = ts.get_k_data(code=code, ktype=ktype, start=start, index=index)
    if index is True:
        code = "INDEX_{}".format(code)
    res = {'code': code, 'ktype': ktype, 'df': klines}
    if res is not None:
        q.put(res)

    return


def writeKlinesToDB(con, q: Queue, timeout: float=5, createTable: bool=False):
    from share.model.dao import KLine

    try:
        obj: dict = q.get(timeout=timeout)
    except:
        return None

    if obj is None:
        return None

    logging.debug("Saving Kline of [{}] type {} in MQ {}".format(obj.get('code'), obj.get('ktype'), q.qsize()))
    klines = obj.get('df')
    res = []
    for _, row in klines.iterrows():
        res.append(KLine.rowToORM(row, "k_{}".format(obj.get('code')), ktype=obj.get('ktype')))

    if createTable:
        logging.debug("Base.metadata.create_all")
        Base.metadata.create_all(con.engine)

    try:
        con.save_all(res, oneByOne=True)
    except:
        logging.debug("Except Base.metadata.create_all")
        Base.metadata.create_all(con.engine)
        con.save_all(res)

    return obj


def writeAllObjsToDB(con: str, q: Queue, timeout: float=5):
    from share.client.SqliteClient import SqliteClient
    from share.model.dao import Base
    dbClient = SqliteClient(base=Base, url=con)
    while True:
        if writeKlinesToDB(dbClient, q, timeout=timeout) is None:
            logging.debug("Nothing more in Queue")
            break
    return


def getKLinesAsync(dbClient, codes, ktype='D', start=None, index=False, multiplier: int=2):
    import multiprocessing
    from multiprocessing import pool

    logging.debug("getKLinesAsync length: {}, type: {}, start: {}".format(
        len(codes), ktype, start.strftime("%Y-%m-%d")))

    threads = multiplier * multiprocessing.cpu_count()

    m = multiprocessing.Manager()
    klineQueue :Queue = m.Queue(maxsize=len(codes)+10)

    workerPool = pool.Pool(threads)


    # Download data to MQ
    for code in codes:
        kwds = {
            'q': klineQueue,
            'code': code,
            'ktype': ktype,
            'start': start,
            'index': index
        }
        workerPool.apply_async(func=downloadKlineToQueue,kwds=kwds,error_callback=logging.warning)

    workerPool.close()

    # Write to DB
    writePool = pool.Pool(threads)
    kwds = {
        'con': dbClient.url,
        'q': klineQueue
    }
    for _ in range(multiplier):
        writePool.apply_async(func=writeAllObjsToDB,kwds=kwds,error_callback=logging.warning)
    writePool.close()

    # Download finished
    workerPool.join()
    klineQueue.put(None)
    writePool.join()

    # Finish all data left
    logging.debug("write joined {} data left in MQ".format(klineQueue.qsize()))
    klineQueue.put(None)
    writeAllObjsToDB(con=dbClient.url, q=klineQueue,timeout=0.1)

    return

