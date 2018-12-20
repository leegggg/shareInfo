import json

'''

        'host':'localhost',
        'port': 8086,
        'user': 'root',
        'passwd': 'root',
        'db':'shareDev'
'''


def getDefaultConfig():
    defaultConfig = {
        "start_r": True,
        "start_days_r": 15,
        "thread_multi": 4,
        "db_url": "sqlite:///./resource.db",
        "log_level": 20,
        "journald": False,
        'influx_host': 'localhost',
        'influx_port': 8086,
        'influx_user': 'root',
        'influx_passwd': 'root',
        'influx_db': 'shareDev'
    }
    return defaultConfig


def getConfig(path: str = "config.json") -> dict:
    default = getDefaultConfig()
    fileConfig = {}
    with open('config.json') as json_data:
        fileConfig = json.load(json_data)
    opt = {**default, **fileConfig}
    return opt


def getInfluxDB(config: dict) -> dict:
    dbinfo = {
        'host': config.get('influx_host'),
        'port': config.get('influx_port'),
        'user': config.get('influx_user'),
        'passwd': config.get('influx_passwd'),
        'db': config.get('influx_db')
    }
    return dbinfo
