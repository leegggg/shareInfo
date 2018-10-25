import json


def getDefaultConfig():
    defaultConfig = {
        "start_r": True,
        "start_days_r": 15,
        "thread_multi": 4,
        "db_url": "sqlite:///./resource.db",
        "log_level": 20,
        "journald": False
    }
    return defaultConfig


def getConfig(path: str="config.json") -> dict:
    default = getDefaultConfig()
    fileConfig = {}
    with open('config.json') as json_data:
        fileConfig = json.load(json_data)
    opt = {**default, **fileConfig}
    return opt

