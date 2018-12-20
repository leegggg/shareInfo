import sys
import logging
from share.client.SqliteClient import SqliteClient
from share.model.dao import Base
import share.service as service
import share.service.tickService as tickService
from datetime import timedelta
from datetime import datetime
from share.util.config import getConfig, getInfluxDB
from share.util import log
from share.client import influxClient


sys.path.insert(0, '.')
sys.path.insert(0, '..')

def main():
    # Load config
    config = getConfig()
    logger = log.getLogger(config)

    logger.info(str(config))
    dbclient = SqliteClient(base=Base, url=config.get('db_url'))

    influxInfo = getInfluxDB(config)
    logger.info(str(influxInfo))
    influx = influxClient.getClient(dbinfo=influxInfo)
    influx.create_database(influxInfo.get('db'))

    # Update Ticks
    logging.info("Daily Update Ticks")
    start = datetime(year=2018, month=3, day=1)
    end = start + timedelta(days=15)
    try:
        codes = service.getAllCodes(dbclient)
        tickService.getTickAsync(
            codes=codes, dbinfo=influxInfo, start=start, end=end, multiplier=config.get('thread_multi'))
    except Exception as e:
        logging.warning("Failed Update Ticks for {}".format(str(e)))

    return


if __name__ == "__main__":
    main()