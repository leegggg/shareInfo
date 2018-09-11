from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def pandaToORM(df, orm):
    res = []
    for _, row in df.iterrows():
        res.append(orm.rowToORM(row))
    return res
