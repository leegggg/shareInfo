import tushare as ts
import logging
from share.model.dao import Base
from datetime import datetime
from datetime import timedelta


def daily(con):
    import share.service.basicInfoService as service
    import tushare as ts

    logging.debug("Daily update of macro")

    import share.service.basicInfoService as service
    import tushare as ts


    import share.model.dao.macro.GdpQuarter as package
    service.getBasicInfo(con=con, package=package, fun=ts.get_gdp_quarter, clean=False)

    import share.model.dao.macro.GdpYear as package
    service.getBasicInfo(con=con, package=package, fun=ts.get_gdp_year, clean=False)

    import share.model.dao.macro.GdpContrib as package
    service.getBasicInfo(con=con, package=package, fun=ts.get_gdp_contrib, clean=False)

    import share.model.dao.macro.GdpFor as package
    service.getBasicInfo(con=con, package=package, fun=ts.get_gdp_for, clean=False)

    import share.model.dao.macro.GdpPull as package
    service.getBasicInfo(con=con, package=package, fun=ts.get_gdp_pull, clean=False)

    import share.model.dao.macro.LoanRate as package
    service.getBasicInfo(con=con, package=package, fun=ts.get_loan_rate, clean=False)

    import share.model.dao.macro.MoneySupply as package
    service.getBasicInfo(con=con, package=package, fun=ts.get_money_supply, clean=False)

    import share.model.dao.macro.MoneySupplyBal as package
    service.getBasicInfo(con=con, package=package, fun=ts.get_money_supply_bal, clean=False)

    import share.model.dao.macro.Ppi as package
    service.getBasicInfo(con=con, package=package, fun=ts.get_ppi, clean=False)

    import share.model.dao.macro.RRR as package
    service.getBasicInfo(con=con, package=package, fun=ts.get_rrr, clean=False)

    import share.model.dao.macro.Cpi as package
    service.getBasicInfo(con=con, package=package, fun=ts.get_cpi, clean=False)

    import share.model.dao.macro.DepositRate as package
    service.getBasicInfo(con=con, package=package, fun=ts.get_deposit_rate, clean=False)

    return

