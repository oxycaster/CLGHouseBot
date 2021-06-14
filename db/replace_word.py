import logging

from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.ext.automap import automap_base

from db.session import engine, session

logger = logging.getLogger(__name__)

Base = automap_base()
Base.prepare(engine, reflect=True)
Base.query = session.query_property()


class ReplaceWord(Base):
    __tablename__ = 'replace_word'

    @classmethod
    def all(cls, session):
        """ fetch all records """
        tbl = cls.classes.replace_word
        return session.query(tbl).all()

    @classmethod
    def add(cls, session, keyword, replace_to):
        tbl = cls.classes.replace_word(keyword=keyword, replace_to=replace_to)
        session.add(tbl)
        try:
            session.commit()
        except InvalidRequestError as e:
            return

    @classmethod
    def delete(cls, session, id):
        tbl = cls.classes.replace_word
        target_record = session.query(tbl).filter_by(id=id).first()
        session.delete(target_record)
        try:
            session.commit()
        except InvalidRequestError as e:
            return target_record
        return target_record
