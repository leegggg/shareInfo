import sys
import logging
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

    # Update BoxOffice
    logging.info("Daily Update BoxOffice")
    from share.service import boxOfficeService
    try:
        boxOfficeService.hourly(con=dbclient)
    except Exception as e:
        logging.warning("Failed Update BoxOffice {}".format(str(e)))

    return


if __name__ == "__main__":
    main()