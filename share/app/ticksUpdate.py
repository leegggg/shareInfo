from datetime import timedelta
from datetime import datetime
import sys
import logging

sys.path.insert(0, '.')
sys.path.insert(0, '..')

from share.client import influxClient
from share.client.SqliteClient import SqliteClient
from share.model.dao import Base
from share.util.config import getConfig, getInfluxDB
from share.util import log
import share.service as service
import share.service.tickService as tickService



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
    start = datetime(year=2018, month=12, day=19)
    #end = start + timedelta(days=15)
    end = datetime.now()
    try:
        codes = service.getAllCodes(dbclient)
        # codes = ['000002']
        tickService.getTickAsync(
            codes=codes, dbinfo=influxInfo, start=start, end=end, multiplier=config.get('thread_multi'))
    except Exception as e:
        logging.warning("Failed Update Ticks for {}".format(str(e)))

    return


if __name__ == "__main__":
    main()