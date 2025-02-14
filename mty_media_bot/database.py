from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class DBManager:
    __engine = None
    __session = None
    dao = None

    @staticmethod
    def init(db_url, db_log_flag=True):
        DBManager.__engine = create_engine(db_url, echo=db_log_flag)
        DBManager.__session = \
            scoped_session(sessionmaker(autocommit=False,
                                        autoflush=False,
                                        bind=DBManager.__engine))

        DBManager.dao = DBManager.__session

    @staticmethod
    def init_db():
        from mty_media_bot.model.music import Music
        from mty_media_bot.model import Base
        Base.metadata.create_all(bind=DBManager.__engine)
