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