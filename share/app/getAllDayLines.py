import sys
sys.path.insert(0, '.')
sys.path.insert(0, '..')


def main():
    import logging
    from share.client.SqliteClient import SqliteClient
    from share.model.dao import Base
    import share.service as service
    import share.service.klineService as getKlines
    from datetime import timedelta
    from datetime import datetime
    import tushare as ts

    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s %(filename)s(%(lineno)d) %(funcName)s(): \t %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    dbclient = SqliteClient(base=Base, url='sqlite:///./share.db')

    # Update Index Klines
    codes = service.getAllIndexCodes()
    start = datetime(year=1990,month=1,day=1)
    start = datetime.now() - timedelta(30)
    getKlines.getKLinesAsync(dbclient, codes=codes, ktype='D', start=start, index=True)

    if codes is not None:
        return

    # Update Klines
    codes = service.getAllCodes(dbclient)
    start = datetime.now() - timedelta(30)
    #start = datetime(year=1990,month=1,day=1)
    getKlines.getKLines(dbclient, codes=codes, ktype='D', start=start)
    getKlines.getKLinesAsync(dbclient,codes=codes,ktype='D',start=start)


    return


if __name__ == "__main__":
    main()