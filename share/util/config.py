import json


def getDefaultConfig():
    defaultConfig = {
        "start_r": True,
        "start_days_r": 15,
        "thread_multi": 4,
        "db_url": "mysql+pymysql://root:dbrootpassword@ada.lan.linyz.net/share-fvt",
        "log_level": 20
    }
    return defaultConfig


def getConfig(path: str="config.json") -> dict:
    default = getDefaultConfig()
    fileConfig = {}
    with open('config.json') as json_data:
        fileConfig = json.load(json_data)
    opt = {**default, **fileConfig}
    return opt

