import sys
import logging
sys.path.insert(0, '.')
sys.path.insert(0, '..')


def main():
    import logging
    from share.client.SqliteClient import SqliteClient
    from share.model.dao import Base

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    dbclient = SqliteClient(base=Base, url='sqlite:///./share.db')

    import share.service.referenceService as service
    from datetime import datetime
    import tushare as ts
    from share.util.dateModel import YearQuarter

    # service.getReports(con=dbclient,fromYearQuarter=YearQuarter.fromDate().__last__())
    service.getAll(con=dbclient,start=datetime(year=1991,month=1,day=1),end=datetime.now())

    return


if __name__ == "__main__":
    main()