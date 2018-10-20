import logging
from share.util.dateModel import YearQuarter
from datetime import datetime
from datetime import timedelta


def downloadReports(year, quarter):
    import tushare as ts

    logging.debug('Getting get_report_data. Of {}Q{}'.format(year,quarter))
    report = ts.get_report_data(year, quarter)

    logging.debug('Getting get_profit_data. Of {}Q{}'.format(year,quarter))
    profitReport = ts.get_profit_data(year, quarter)
    report = report.join(other=profitReport.set_index('code'), on='code', rsuffix='_profit', how='left')

    logging.debug('Getting get_operation_data. Of {}Q{}'.format(year,quarter))
    operationReport = ts.get_operation_data(year, quarter)
    report = report.join(other=operationReport.set_index('code'), on='code', rsuffix='_operation', how='left')

    logging.debug('Getting get_growth_data. Of {}Q{}'.format(year,quarter))
    growthReport = ts.get_growth_data(year, quarter)
    report = report.join(other=growthReport.set_index('code'), on='code', rsuffix='_growth', how='left')

    logging.debug('Getting get_debtpaying_data. Of {}Q{}'.format(year,quarter))
    debtpayingReport = ts.get_debtpaying_data(year, quarter)
    report = report.join(other=debtpayingReport.set_index('code'), on='code', rsuffix='_debtpaying', how='left')

    logging.debug('Getting get_cashflow_data. Of {}Q{}'.format(year,quarter))
    cashflowReport = ts.get_cashflow_data(year, quarter)
    report = report.join(other=cashflowReport.set_index('code'), on='code', rsuffix='_cashflow', how='left')

    return report


def getReport(con, yearQuarter):
    from share.model.dao import Base
    from share.model.dao.report import ReportMain as Model

    if yearQuarter is None:
        yearQuarter = YearQuarter.fromDate().__last__()

    logging.debug('Getting reports of {}.'.format(yearQuarter))

    report = downloadReports(year=yearQuarter.year, quarter=yearQuarter.quarter)

    res = []
    for _, row in report.iterrows():
        res.append(Model.rowToORM(row=row, year=yearQuarter.year, quarter=yearQuarter.quarter))
    Base.metadata.create_all(con.engine)
    con.save_all(res)
    return


def getReports(con, fromYearQuarter,toYearQuarter=None):
    from share.util.dateModel import YearQuarter
    if toYearQuarter is None:
        toYearQuarter = YearQuarter.fromDate()

    current = fromYearQuarter
    while not current.__ge__(toYearQuarter):
        try:
            getReport(con=con, yearQuarter=current)
        except OSError:
            logging.info('Failed to get report of {}.'.format(current))
        except TypeError:
            logging.info('Failed to get report of {}.'.format(current))

        current = current.__next__()


def getBasicReport(con, clean=False):
    from share.model.dao import Base
    import share.model.dao.report.ReportBasic as package
    import tushare as ts

    logging.debug("Updateing {} classified".format(package.__name__))
    df = ts.get_stock_basics()
    res = []
    for index, row in df.iterrows():
        res.append(package.rowToORM(row=row,code=index))
    Base.metadata.create_all(con.engine)
    if clean is True and len(res)>0:
        con.delete_all(res[0].__class__)
    con.save_all(res)
    return


def daily(con):
    logging.debug("Daily update of Reports")

    getBasicReport(con=con)

    end = YearQuarter.fromDate(date=datetime.now())
    start = YearQuarter.fromDate(date=datetime.now() - timedelta(days=180))

    getReports(con=con,fromYearQuarter=start,toYearQuarter=end)

    return