import sys
import logging
sys.path.insert(0, '.')
sys.path.insert(0, '..')


def main():
    import logging
    from share.client.SqliteClient import SqliteClient
    from share.model.dao import Base
    from share.util.config import getConfig

    # Load config
    config = getConfig()

    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s %(filename)s(%(lineno)d) %(funcName)s(): \t %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(config.get('log_level'))

    logging.info(str(config))
    dbclient = SqliteClient(base=Base, url=config.get('db_url'))

    import share.service.referenceService as service
    from datetime import datetime
    import tushare as ts
    from share.util.dateModel import YearQuarter

    # service.getReports(con=dbclient,fromYearQuarter=YearQuarter.fromDate().__last__())
    service.getAll(con=dbclient,start=datetime(year=1991,month=1,day=1),end=datetime.now())

    return


if __name__ == "__main__":
    main()