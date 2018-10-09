import unittest
from share.client.SqliteClient import SqliteClient
from share.model import Base
import tushare as ts


class Test(unittest.TestCase):
    def __init__(self):
        self.dbclient = SqliteClient(base=Base, url='sqlite:///./test.db')

    def test_get_report_main(self):
        from datetime import datetime
        from share.model.dao.report import ReportMain

        print(datetime.now())
        year = datetime.now().year - 1
        quarter = 1
        reports = ts.get_report_data(year, quarter)
        print(datetime.now())

        res = []
        for _, row in reports.iterrows():
            res.append(ReportMain.rowToORM(row, year, quarter))

        print(datetime.now())

        Base.metadata.create_all(self.dbclient.engine)

        self.dbclient.save_all(res)
        print(datetime.now())

    def test_get_report_profit(self):
        from datetime import datetime
        from share.model import ReportProfit

        print(datetime.now())
        year = datetime.now().year - 1
        quarter = 1
        reports = ts.get_profit_data(year, quarter)
        print(datetime.now())

        res = []
        for _, row in reports.iterrows():
            res.append(ReportProfit.rowToORM(row, year, quarter))

        print(datetime.now())

        Base.metadata.create_all(self.dbclient.engine)

        self.dbclient.save_all(res)
        print(datetime.now())