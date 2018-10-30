import logging



def getBasicInfo(con, package, fun, clean=True):
    from share.model.dao import Base

    logging.debug("Updateing {} with basicInfoService".format(package.__name__))
    df = fun()
    res = []
    for _, row in df.iterrows():
        r = package.rowToORM(row)
        if r is not None:
            res.append(r)
    Base.metadata.create_all(con.engine)
    if clean is True and len(res)>0:
        con.delete_all(res[0].__class__)
    con.save_all(res)
    return

