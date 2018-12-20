from share.util.numberUtil import toFloat, toInt, toStr
from datetime import tzinfo, timedelta, datetime
from dateutil import parser

TIME_ZONE_OFFSET_SECONDS = 8 * 3600

def rowToORM(row, code:str, currentStr:str):
    tsStr = "{}T{}".format(currentStr, toStr(row.loc['time']))
    # timestamp = datetime.fromisoformat(tsStr)  # Only for py3.7+
    timestamp = parser.parse(tsStr)
    timestamp = timestamp - timedelta(seconds=TIME_ZONE_OFFSET_SECONDS)
    typeStr = toStr(row.loc['type'])
    influxPoint = {
        "measurement": "share_tick",
        "tags": {
            "code": code
        },
        "time": timestamp,
        "fields": {
            "price": toFloat(row.loc['price']),
            "change": toFloat(row.loc['change']),
            "volume": toInt(row.loc['volume']),
            "amount": toInt(row.loc['amount']),
            "type_buy": typeStr == '买盘',
            "type_sell": typeStr == '卖盘',
            "type_neutral": typeStr == '中性盘'
        }
    }
    return influxPoint