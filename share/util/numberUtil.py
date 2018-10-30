from datetime import datetime

def toFloat(string):
    res = None
    try:
        res = float(string)
    except ValueError:
        pass

    # Nan
    if not res is None:
        if not (res <= 0 or res >= 0):
            res = None

    return res


def toInt(string):
    res = None
    try:
        res = int(string)
    except ValueError:
        pass

    # Nan
    if not res is None:
        if not (res <= 0 or res >= 0):
            res = None

    return res


def toStr(string):
    res = str(string)
    if string != string:
        res = None
    return res


def dateTimeToTsStr(dt: datetime) -> str:
    import struct
    import base64
    bytesTs = struct.pack('<d', dt.timestamp())
    return base64.b64encode(bytesTs).decode('UTF-8')