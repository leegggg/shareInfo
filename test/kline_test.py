import unittest


class Test(unittest.TestCase):
    def test_get_latest_news(self):
        import tushare as ts
        from share.client.SqliteClient import SqliteClient
        from share.model import Base
        from datetime import datetime
        from share.model.dao import KLine
        dbclient = SqliteClient(base=Base, url='sqlite:///./test.db')
        # get_report_data(2017, 3, engine)
        # rep = ts.cap_tops()
        code = '601766'
        type = 'D'
        print(datetime.now())
        klines = ts.get_k_data(code=code, ktype=type, start='2018-01-01')
        print(datetime.now())
        res = []
        for _, row in klines.iterrows():
            res.append(KLine.rowToORM(row, "k_{}_{}".format(code, type)))
        print(datetime.now())

        Base.metadata.create_all(dbclient.engine)

        dbclient.save_all(res)
        print(datetime.now())