def toFloat(string):
    res = float('nan')
    try:
        res = float(string)
    except ValueError:
        pass
    return res


def toInt(string):
    res = float('nan')
    try:
        res = int(string)
    except ValueError:
        pass
    return res