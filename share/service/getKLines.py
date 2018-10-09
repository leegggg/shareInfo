import logging


def updateKline(code, con, ktype='D', start=None):
    import tushare as ts
    from share.model.dao import KLine
    from share.model.dao import Base
    from datetime import datetime
    from datetime import timedelta

    if start is None:
        start = datetime.now() - timedelta(days=90)
    start = start.strftime('%Y-%m-%d')

    logging.debug("Kline of [{}] type {} from {}".format(code, ktype ,start))
    klines = ts.get_k_data(code=code, ktype=ktype, start=start)
    res = []
    for _, row in klines.iterrows():
        res.append(KLine.rowToORM(row, "k_{}_{}".format(code, ktype)))
    Base.metadata.create_all(con.engine)
    con.save_all(res)
    return


def getKLines(dbClient, codes, ktype='D', start=None):
    from datetime import datetime
    from datetime import timedelta
    if start is None:
        start = datetime.now() - timedelta(days=90)

    for code in codes:
        updateKline(code, dbClient, ktype, start)
    return
