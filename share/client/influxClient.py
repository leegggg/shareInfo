from influxdb import InfluxDBClient


def getClient(dbinfo:dict)->InfluxDBClient:
    influxClient = InfluxDBClient(
        host=dbinfo.get('host'),
        port=dbinfo.get('port'),
        username=dbinfo.get('user'),
        password=dbinfo.get('passwd'),
        database=dbinfo.get('db')
    )
    return influxClient