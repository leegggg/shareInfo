from . import DBClient as DBClient
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker


class SqliteClient(DBClient.DBClient):

    def __init__(self, base, url='sqlite:///./resource.db'):
        self.url = url
        self.base = base
        self.engine = create_engine(url)
        base.metadata.create_all(self.engine)
        self.DBSession = sessionmaker(bind=self.engine)

    def new(self):
        return SqliteClient(base=self.base,url=self.url)

    def delete_all(self, model):
        session = self.DBSession()
        try:
            session.query(model).delete()
            session.commit()
        except:
            raise
        finally:
            session.close()
        return

    def save(self, orm):
        session = self.DBSession()
        try:
            session.merge(orm)
            session.commit()
        except:
            raise
        finally:
            session.close()
        return

    def save_all(self, orms):
        session = self.DBSession()
        try:
            for orm in orms:
                session.merge(orm)
            session.commit()
        except:
            raise
        finally:
            session.close()
        return