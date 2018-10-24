from . import DBClient as DBClient
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
import logging

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

    def save(self, orm, onDup: str='ignore'):
        session = self.DBSession()
        try:
            session.merge(orm)
            session.commit()
        except IntegrityError as e:
            logging.log(logging.DEBUG, "Skip a record with {}".format(str(e)))
        except Exception:
            raise
        finally:
            session.close()
        return

    def save_all(self, orms, oneByOne=False):
        if oneByOne is True:
            for orm in orms:
                self.save(orm)
            return

        session = self.DBSession()

        try:
            for orm in orms:
                session.merge(orm)
            session.commit()
        except IntegrityError as e:
            logging.warning("Bulk write with error try on by one with {}".format(str(e)))
            for orm in orms:
                self.save(orm)
        except Exception as e:
            logging.warning("Write failed with:".format(str(e)))
            raise
        finally:
            session.close()
        return

