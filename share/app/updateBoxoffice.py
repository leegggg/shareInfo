import sys
import logging
from datetime import datetime
from datetime import timedelta
from share.util import config as Config


sys.path.insert(0, '.')
sys.path.insert(0, '..')


def main():
    import logging
    from share.client.SqliteClient import SqliteClient
    from share.model.dao import Base

    config = Config.getConfig()
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s %(filename)s(%(lineno)d) %(funcName)s(): \t %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(config.get('log_level'))
    logging.info(config)
    dbclient = SqliteClient(base=Base, url=config.get("db_url"))

    import share.service.boxOfficeService as service
    import tushare as ts
    from share.util.dateModel import YearQuarter

    # service.getReports(con=dbclient,fromYearQuarter=YearQuarter.fromDate().__last__())

    # from share.service import boxOfficeService
    # boxOfficeService.daily(con=dbclient)
    service.daily(con=dbclient)
    # return

    service.updateDayBoxoffice(con=dbclient, date=datetime.now())
    service.updateRealtimeBoxoffice(con=dbclient)

    date = datetime(year=2010,month=3,day=1)
    while date.timestamp() < datetime.now().timestamp():
        logging.info("Update box office data of {}".format(date.strftime("%Y-%m-%d")))

        try:
            service.updateDayCinema(con=dbclient, date=date)
        except:
            logging.warning("Failed Update updateDayCinema data of {}".format(date.strftime("%Y-%m-%d")))

        if date.day == 15:
            try:
                service.updateMonthBoxoffice(con=dbclient, year=date.year,month=date.month)
            except:
                logging.warning("Failed Update updateMonthBoxoffice data of {}".format(date.strftime("%Y-%m-%d")))

        date = date + timedelta(days=1)

    return


if __name__ == "__main__":
    main()