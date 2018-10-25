import sys
import logging
sys.path.insert(0, '.')
sys.path.insert(0, '..')


def main():
    import logging
    from share.client.SqliteClient import SqliteClient
    from share.model.dao import Base
    from share.util.config import getConfig
    from share.util import log
    from share.util.config import getConfig

    # Load config
    config = getConfig()
    logger = log.getLogger(config)
    logging.info(str(config))
    dbclient = SqliteClient(base=Base, url=config.get('db_url'))

    import share.service.reportService as service
    import tushare as ts
    from share.util.dateModel import YearQuarter

    # service.getReports(con=dbclient,fromYearQuarter=YearQuarter.fromDate().__last__())
    service.getReports(con=dbclient, fromYearQuarter=YearQuarter(year=1985,quarter=3))

    return


if __name__ == "__main__":
    main()