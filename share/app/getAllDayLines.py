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
    from share.util.config import getConfig
    from share.util import log

    # Load config
    config = getConfig()
    logger = log.getLogger(config)
    logging.info(str(config))
    dbclient = SqliteClient(base=Base, url=config.get('db_url'))


    # Update Klines
    codes = service.getAllCodes(dbclient)
    start = datetime(year=1990,month=1,day=1)
    getKlines.getKLines(dbclient, codes=codes, ktype='D', start=start)
    getKlines.getKLinesAsync(dbclient,codes=codes,ktype='D',start=start)

    # # Update Index Klines
    # codes = service.getAllIndexCodes()
    # start = datetime(year=1990,month=1,day=1)
    # getKlines.getKLinesAsync(dbclient, codes=codes, ktype='D', start=start, index=True)



    return


if __name__ == "__main__":
    main()