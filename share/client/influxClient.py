from influxdb import InfluxDBClient
from influxdb import DataFrameClient


def getClient(dbinfo:dict)->InfluxDBClient:
    influxClient = InfluxDBClient(
        host=dbinfo.get('host'),
        port=dbinfo.get('port'),
        username=dbinfo.get('user'),
        password=dbinfo.get('passwd'),
        database=dbinfo.get('db')
    )
    return influxClient


def getDataFrameClient(dbinfo:dict)->DataFrameClient:
    client = DataFrameClient(
        host=dbinfo.get('host'),
        port=dbinfo.get('port'),
        username=dbinfo.get('user'),
        password=dbinfo.get('passwd'),
        database=dbinfo.get('db')
    )
    return client

