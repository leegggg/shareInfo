import tushare as ts
from share import service as ShareService
from share.client.SqliteClient import SqliteClient
from influxdb import InfluxDBClient
from share.util.numberUtil import toFloat, toInt, toStr
from datetime import tzinfo, timedelta, datetime
from share.model.dao import tick


TICK_TYPES = {
    '买盘':1,
    '中性盘':0,
    '卖盘':-1
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
    logging.info(str(config))
    dbclient = SqliteClient(base=Base, url=config.get('db_url'))
    influxClient = InfluxDBClient('localhost', 8086, 'root', 'root', 'example')
    influxClient.create_database('shareDev')

    code = '000001'
    start = datetime(year=2018,month=3,day=1)
    end = datetime.now()

    current = start
    while current < end:
        # Weekends
        if current.weekday() >= 5:
            current = current + timedelta(days=1)
            continue

        currentStr = current.strftime("%Y-%m-%d")
        logger.info("code: {}, date: {}".format(code,currentStr))
        ticks = ts.get_tick_data(code=code, date=currentStr, src='tt')
        if ticks is None:
            logger.info("Skip")
            current = current + timedelta(days=1)
            continue

        points = []
        for _, row in ticks.iterrows():
            points.append(tick.rowToORM(row=row,code=code,currentStr=currentStr))

        influxClient.write_points(points=points, database='shareDev')
        current = current + timedelta(days=1)
    pass

if __name__ == '__main__':
    main()