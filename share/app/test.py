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
from pandas import DataFrame
from pandas import Series

TICK_TYPES = {
    '买盘': 1,
    '中性盘': 0,
    '卖盘': -1
}


def getDataXMax(code: str, influx: DataFrameClient,start: datetime, end: datetime) -> DataFrame:
    query = '''
    SELECT max("price") AS "max"
        FROM "shareDev"."autogen"."share_tick" 
        WHERE 
                time > '{start:s}Z' 
            AND time < '{end:s}Z' 
            AND ("code"='{code:s}')
        GROUP BY time(3h), "code"  fill(linear)
    '''.format(code=code, start=start.isoformat(timespec="milliseconds"), end=end.isoformat(timespec="milliseconds"))
    step = int(5 * 24 / 3)  # 5days * 24h / 3h (pts)

    df = influx.query(query).get(('share_tick', (('code', code),)))
    df['max'].fillna(method='backfill', inplace=True)
    df['max'].fillna(method='ffill', inplace=True)

    source = pd.Series(df['max'], index=df.index)
    # calc rolling max of step and shift steps
    # maxR_d-5
    res = source.rolling(step).max()  # .shift(-1*step)
    result: Series = res.combine(source, lambda r, s: (r - s) / s)
    result: DataFrame = result.to_frame()
    indexName = '{code:s}_maxR_d-5'.format(code=code)
    result.columns = [indexName]

    return result

def getDataYMax(code: str, influx: DataFrameClient,start: datetime, end: datetime) -> DataFrame:
    query = '''
    SELECT max("price") AS "max"
        FROM "shareDev"."autogen"."share_tick" 
        WHERE 
                time > '{start:s}Z' 
            AND time < '{end:s}Z' 
            AND ("code"='{code:s}')
        GROUP BY time(3h), "code"  fill(linear)
    '''.format(code=code, start=start.isoformat(timespec="milliseconds"), end=end.isoformat(timespec="milliseconds"))
    step = int(5 * 24 / 3)  # 5days * 24h / 3h (pts)

    df = influx.query(query).get(('share_tick', (('code', code),)))
    df['max'].fillna(method='backfill', inplace=True)
    df['max'].fillna(method='ffill', inplace=True)

    source = pd.Series(df['max'], index=df.index)
    # calc rolling max of step and shift steps
    # maxR_d-5
    res = source.rolling(step).max()  # .shift(-1*step)
    result: Series = res.combine(source, lambda r, s: (r - s) / s)
    result: DataFrame = result.to_frame()
    indexName = '{code:s}_maxR_d-5'.format(code=code)
    result.columns = [indexName]

    return result


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

    start = datetime(year=2018, month=6, day=1,hour=0,minute=0,second=0)
    end = datetime(year=2019, month=1, day=8, hour=2, minute=10, second=0)

    codes = []
    codesSql = '''
        SELECT DISTINCT code
        FROM `share-fvt`.CLASSIFIED_HS300S
        WHERE `date`='2019-01-30';
    '''
    codeDF = pd.read_sql_query(codesSql, dbclient.engine)
    for _, row in codeDF.iterrows():
        code = row.loc['code']
        codes.append(code)

    # query = '''
    # SELECT
    #     (max("price")-first("price"))/first("price") AS "max_price",
    #     (min("price")-first("price"))/first("price") AS "min_price"
    # FROM "shareDev"."autogen"."share_tick"
    # WHERE
    #     time > now() - 180d
    #     AND ("code"='000001' OR "code"='000001')
    # GROUP BY time(5d), "code"  fill(null)
    # '''

    xSet:DataFrame = None
    for code in codes:
        res = getDataXMax(code,influx,start,end)
        if xSet is None:
            xSet = res
        else:
            xSet = pd.concat([xSet, res], axis=1, join_axes=[xSet.index])

    xSet.to_pickle('./xSet.pickle')
    pass



if __name__ == '__main__':
    main()
