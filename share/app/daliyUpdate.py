import sys
import logging
sys.path.insert(0, '.')
sys.path.insert(0, '..')

config = {
    'start_days_r': 8,
    'start_r': True,
    'start_days_r': 15,
    'db_url': 'mysql+pymysql://root:dbrootpassword@ada.lan.linyz.net/share-fvt'
}





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

    dbclient = SqliteClient(base=Base, url=config.get('db_url'))

    # Update Reference
    logging.info("Daily Update Reference")
    import share.service.referenceService as referenceService
    try:
        referenceService.daily(con=dbclient)
    except Exception as e:
        logging.warning("Failed Daily Update Reference {}".format(str(e)))

    # Update classified
    logging.info("Daily Update classified")
    from share.service import classifiedService
    try:
        classifiedService.daily(con=dbclient)
    except Exception as e:
        logging.warning("Failed Update classified {}".format(str(e)))
        raise

    # Update BoxOffice
    logging.info("Daily Update BoxOffice")
    from share.service import boxOfficeService
    try:
        boxOfficeService.daily(con=dbclient)
    except Exception as e:
        logging.warning("Failed Update BoxOffice {}".format(str(e)))

    # Update macro
    logging.info("Daily Update macro")
    from share.service import macroService
    try:
        macroService.daily(con=dbclient)
    except Exception as e:
        logging.warning("Failed Daily Update macro {}".format(str(e)))

    # Update reports
    logging.info("Daily Update reports")
    from share.service import reportService
    try:
        reportService.daily(con=dbclient)
    except Exception as e:
        logging.warning("Failed Update reports {}".format(str(e)))

    # Update Index Klines
    logging.info("Daily Update Index Klines")
    start = datetime.now() - timedelta(config.get('start_days_r'))
    try:
        codes = service.getAllIndexCodes()
        getKlines.getKLinesAsync(dbClient=dbclient, codes=codes, ktype='D', start=start, index=True, multiplier=4)
    except Exception as e:
        logging.warning("Failed Update index Klines {}".format(str(e)))


    # Update Klines
    logging.info("Daily Update Klines")
    start = datetime.now() - timedelta(config.get('start_days_r'))
    try:
        codes = service.getAllCodes(dbclient)
        getKlines.getKLinesAsync(codes=codes,dbClient=dbclient,ktype='D',start=start)
    except:
        logging.warning("Failed Update Klines")

    logging.info("All tasks finished, big brother is watching.")
    return


if __name__ == "__main__":
    main()