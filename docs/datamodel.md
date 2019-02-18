#

## source

source

```text
ts            price
1550475394    10.1
+3s           10.2
...
```

target

```text
             |                                X                                       |    Y
-------------+------------------------------------------------------------------------+---------------
ts            000001-maxR-d-5  000001-minR-d-5  000001-last-d-5  000002-maxR-d-5  .... 000001-maxR-d+5
1550475394    
+3600*24
+3600*24
+3600*24
```

function

```python
def calc(subset,func):
    return (func(subset)-last(subset)) / last(subset)


def getDataX(code,source,step=5d):
    current = first

    target = df([{code-maxR-d-5,code-minR-d-5,...}])
    for current<now:
        subset = source[current,current-step]

        if OutOfRange:
            target.append({none,none,...})
            break

        res = {calc(subset,max),calc(subset,min),...}
        target.append(res)

    target = """
    ts            000001-maxR-d-5  000001-minR-d-5  000001-last-d-5  000002-maxR-d-5  .... 000001-maxR-d+5
    1550475394    none
    +3600*24      none
    +3600*24      none
    +3600*24      none
    +3600*24      none
    +3600*24      0.1
    ...
    +3600*24      0.2
    """
    return target

def calcLater(subset,func):
    return (func(subset)-first(subset)) / first(subset)

def getDataY(code,source,step=5d):
    current = first

    target = df([{code-maxR-d+5}])
    for current<now:
        subset = source[current,current+step]

        if OutOfRange:
            target.append({none,none,...})
            break

        res = {calc(subset,max),calc(subset,min),...}
        target.append(res)

    target = """
    ts            000001-maxR-d+5
    1550475394    0.1
    +3600*24      0.2
    ...
    +3600*24      -0.1
    +3600*24      none
    +3600*24      none
    +3600*24      none
    +3600*24      none
    +3600*24      none
    """
    return target

source = '''
    select price as price from influx
    where time in [first,now]
    and {code}
    groupby 1d fill linear'''

codeXs = ['000001','000002','000003',...]
codeYs = ['000001']

dataX = df()
for code in codeXs:
    dataX =dataX.merge(getCodeX(code,source))

dataY = getCodeX(codeY,source)

target = dataX.merge(dataY)

target = '''
             |                                X                                       |    Y
-------------+------------------------------------------------------------------------+---------------
ts           |000001-maxR-d-5  000001-minR-d-5  000001-last-d-5  000002-maxR-d-5  ....|000001-maxR-d+5
-------------+------------------------------------------------------------------------+---------------
1550475394   |none                                                                    |0.1
+3600*24     |none                                                                    |0.2
+3600*24     |none                                                                    |0.3
+3600*24     |none                                                                    |0.4
+3600*24     |none                                                                    |0.5
+3600*24     |0.6                                                                     |0.6
...
+3600*24     |-0.6                                                                    |-0.6
+3600*24     |-0.5                                                                    |none
+3600*24     |-0.4                                                                    |none
+3600*24     |-0.3                                                                    |none
+3600*24     |-0.2                                                                    |none
-------------+------------------------------------------------------------------------|---------------
today1500    |-0.1                                                                    |none
'''

```