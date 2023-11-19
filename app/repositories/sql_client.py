import urllib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from databases import Database

class SQLClient:
    def __init__(self):
        try:
            engine = create_engine("sqlite:///pyladies.db", echo=True)
            self.__session = sessionmaker(
                autocommit=False, autoflush=False, bind=engine)
        except Exception as e:
            raise

    
    def get_session(self):
        return self.__session()


sql_client = SQLClient()
