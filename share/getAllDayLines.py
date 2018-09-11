import sys
sys.path.insert(0, '.')
sys.path.insert(0, '..')

import tushare as ts
import pandas

from share.model.AreaClassified import AreaClassified as AreaClassified
from sqlalchemy import create_engine
import share.model.AreaClassified as areaClassified
from share.client.SqliteClient import SqliteClient as SqliteClient
import share.model as tushareTable
from share.model import Base
from share.client.SqliteClient import SqliteClient
from share.model import Base
from datetime import datetime
from share.model import KLine
from datetime import datetime


def get_report_data(year, quarter, engine):
    report = ts.get_report_data(year=year, quarter=quarter)
    print(report)
    report.to_sql(
        name="report_data", con=engine, if_exists='replace', index=True)
    return


def updateKline(code, con, type='D', start='1990-01-01'):
    print("{} ====== {} ==============".format(code,
                                               datetime.now().isoformat()))
    klines = ts.get_k_data(code=code, ktype=type, start=start)
    print(datetime.now())
    res = []
    for _, row in klines.iterrows():
        res.append(KLine.rowToORM(row, "k_{}_{}".format(code, type)))
    print(datetime.now())
    Base.metadata.create_all(con.engine)
    con.save_all(res)
    print(datetime.now())
    return


def main():
    dbclient = SqliteClient(base=Base, url='sqlite:///./share.db')
    # get_report_data(2017, 3, engine)
    # rep = ts.cap_tops()
    codesSql = 'select code from AREA_CLASSIFIED;'
    codes = pandas.read_sql_query(codesSql, dbclient.engine)
    for _, row in codes.iterrows():
        code = row.loc['code']
        updateKline(code, dbclient, type='D', start='1990-01-01')
    return


if __name__ == "__main__":
    main()