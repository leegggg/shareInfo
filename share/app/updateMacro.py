import sys

sys.path.insert(0, '.')
sys.path.insert(0, '..')



def main():
    import logging
    from share.client.SqliteClient import SqliteClient
    from share.model.dao import Base


    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    dbclient = SqliteClient(base=Base, url='sqlite:///./share.db')

    import share.service.basicInfoService as service
    import tushare as ts


    import share.model.dao.macro.GdpQuarter as package
    service.getBasicInfo(con=dbclient, package=package, fun=ts.get_gdp_quarter, clean=False)

    import share.model.dao.macro.GdpYear as package
    service.getBasicInfo(con=dbclient, package=package, fun=ts.get_gdp_year, clean=False)

    import share.model.dao.macro.GdpContrib as package
    service.getBasicInfo(con=dbclient, package=package, fun=ts.get_gdp_contrib, clean=False)

    import share.model.dao.macro.GdpFor as package
    service.getBasicInfo(con=dbclient, package=package, fun=ts.get_gdp_for, clean=False)

    import share.model.dao.macro.GdpPull as package
    service.getBasicInfo(con=dbclient, package=package, fun=ts.get_gdp_pull, clean=False)

    import share.model.dao.macro.LoanRate as package
    service.getBasicInfo(con=dbclient, package=package, fun=ts.get_loan_rate, clean=False)

    import share.model.dao.macro.MoneySupply as package
    service.getBasicInfo(con=dbclient, package=package, fun=ts.get_money_supply, clean=False)

    import share.model.dao.macro.MoneySupplyBal as package
    service.getBasicInfo(con=dbclient, package=package, fun=ts.get_money_supply_bal, clean=False)

    import share.model.dao.macro.Ppi as package
    service.getBasicInfo(con=dbclient, package=package, fun=ts.get_ppi, clean=False)

    import share.model.dao.macro.RRR as package
    service.getBasicInfo(con=dbclient, package=package, fun=ts.get_rrr, clean=False)

    import share.model.dao.macro.Cpi as package
    service.getBasicInfo(con=dbclient, package=package, fun=ts.get_cpi, clean=False)

    import share.model.dao.macro.DepositRate as package
    service.getBasicInfo(con=dbclient, package=package, fun=ts.get_deposit_rate, clean=False)

    return


if __name__ == "__main__":
    main()