import tushare as ts
from share import service as ShareService
from share.client.SqliteClient import SqliteClient
from influxdb import InfluxDBClient
from share.util.numberUtil import toFloat, toInt, toStr
from datetime import tzinfo, timedelta, datetime
from share.model.dao import tick
from share.util.config import getConfig, getInfluxDB
from share.client import influxClient
from influxdb import DataFrameClient
import pandas as pd

TICK_TYPES = {
    '买盘': 1,
    '中性盘': 0,
    '卖盘': -1
}


def main():
    import logging
    from share.client.SqliteClient import SqliteClient
    from share.model.dao import Base
    from share.util.config import getConfig
    from share.util import log

    # Load config
    config = getConfig()
    logger = log.getLogger(config)

    logger.info(str(config))
    dbclient = SqliteClient(base=Base, url=config.get('db_url'))

    influxInfo = getInfluxDB(config)
    logger.info(str(influxInfo))
    influx = influxClient.getDataFrameClient(influxInfo)
    influx.create_database(influxInfo.get('db'))

    code = '000001'
    start = datetime(year=2018, month=3, day=1)
    end = datetime.now()


    query = '''
    SELECT mean("price") AS "mean_price" 
        FROM "shareDev"."autogen"."share_tick" 
        WHERE 
                time > '2018-06-01T02:10:00.000Z' 
            AND time < '2019-01-08T02:10:00.000Z' 
            AND ("code"='000001' OR "code"='000002')
        GROUP BY time(5d), "code"
    '''

    query = '''
    SELECT 
        (max("price")-first("price"))/first("price") AS "max_price", 
        (min("price")-first("price"))/first("price") AS "min_price"
    FROM "shareDev"."autogen"."share_tick" 
    WHERE 
        time > now() - 180d 
        AND ("code"='000001' OR "code"='000001') 
    GROUP BY time(5d), "code"  fill(null)
    '''

    print("Read DataFrame")
    df = influx.query(query)

    pass


if __name__ == '__main__':
    main()
