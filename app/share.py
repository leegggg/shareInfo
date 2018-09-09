import tushare as ts
from model.AreaClassified import AreaClassified as AreaClassified
from sqlalchemy import create_engine
import model.AreaClassified as areaClassified
from client.SqliteClient import SqliteClient as SqliteClient
import model as tushareTable
from model import Base

from datetime import datetime


def get_report_data(year, quarter, engine):
    report = ts.get_report_data(year=year, quarter=quarter)
    print(report)
    report.to_sql(
        name="report_data", con=engine, if_exists='replace', index=True)
    return


def main():
    dbclient = SqliteClient(base=Base, url='sqlite:///./share.db')
    # get_report_data(2017, 3, engine)
    # rep = ts.cap_tops()
    print(datetime.now())
    areas = ts.get_area_classified()
    print(datetime.now())
    areas = tushareTable.pandaToORM(areas, areaClassified)
    print(datetime.now())
    dbclient.save_all(areas)
    print(datetime.now())

    return


if __name__ == "__main__":
    main()