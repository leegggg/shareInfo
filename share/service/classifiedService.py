import tushare as ts
import logging
from share.model.dao import Base
from datetime import datetime
from datetime import timedelta


def daily(con):
    import share.service.basicInfoService as service
    import tushare as ts

    logging.debug("Daily update of classified")

    # Update Suspended classified
    # import share.model.ClassifiedSuspended as package
    # service.getClassified(con=dbclient,package=package,fun=ts.get_suspended,clean=False)

    #  Update Terminated classified
    # import share.model.ClassifiedTerminated as package
    # service.getClassified(con=dbclient,package=package,fun=ts.get_terminated,clean=False)

    # Update HS300 classified
    import share.model.dao.classified.ClassifiedHS300S as package
    service.getBasicInfo(con=con, package=package, fun=ts.get_hs300s, clean=False)

    # Update SZ50 classified
    import share.model.dao.classified.ClassifiedSZ50s as package
    service.getBasicInfo(con=con, package=package, fun=ts.get_sz50s)

    # Update ZZ500 classified
    import share.model.dao.classified.ClassifiedZZ500S as package
    service.getBasicInfo(con=con, package=package, fun=ts.get_zz500s)

    # Update St classified
    import share.model.dao.classified.ClassifiedSt as package
    service.getBasicInfo(con=con, package=package, fun=ts.get_st_classified)

    # Update Gem classified
    import share.model.dao.classified.ClassifiedGem as package
    service.getBasicInfo(con=con, package=package, fun=ts.get_gem_classified)

    # Update Sme classified
    import share.model.dao.classified.ClassifiedSme as package
    service.getBasicInfo(con=con, package=package, fun=ts.get_sme_classified)

    # Update area classified
    import share.model.dao.classified.ClassifiedArea as package
    service.getBasicInfo(con=con, package=package, fun=ts.get_area_classified)

    # Update concept classified
    import share.model.dao.classified.ClassifiedConcept as package
    service.getBasicInfo(con=con, package=package, fun=ts.get_concept_classified)

    # Update industry classified
    import share.model.dao.classified.ClassifiedIndustry as package
    service.getBasicInfo(con=con, package=package, fun=ts.get_industry_classified)

    return

