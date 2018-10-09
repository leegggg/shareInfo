import sys
import logging
sys.path.insert(0, '.')
sys.path.insert(0, '..')

config = {
    'start_days_r': 8,
    'start_r': True,
    'start_days_r': 15,
    'db_url': 'sqlite:///./share.db'
}





def main():
    import logging
    from share.client.SqliteClient import SqliteClient
    from share.model.dao import Base
    import share.service as service
    import share.service.getKLines as getKlines
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

    # Update Stock basic classified
    import share.service.getReportService as reportService
    reportService.getBasicReport(con=dbclient)

    # Update Klines
    start = datetime.now() - timedelta(config.get('start_days_r'))
    codes = service.getAllCodes(dbclient)
    getKlines.getKLines(codes=codes,dbClient=dbclient,ktype='D',start=start)

    # Update BoxOffice
    from share.service import boxOfficeService
    date = datetime.now()
    boxOfficeService.updateDayBoxoffice(con=dbclient, date=date)
    boxOfficeService.updateDayCinema(con=dbclient, date=date)


    return


if __name__ == "__main__":
    main()