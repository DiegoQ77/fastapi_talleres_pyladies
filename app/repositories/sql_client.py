import urllib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from databases import Database


class ConnectionStringBuilder:
    @staticmethod
    def get_default_connection_string():

        # if DatabaseConfig.get_type() == "sql_server":
        #     connection_attributes = urllib.parse.quote_plus(
        #         f"DRIVER={DatabaseConfig.get_driver()};"
        #         f"SERVER={DatabaseConfig.get_server()};"
        #         f"DATABASE={DatabaseConfig.get_database()};"
        #         f"UID={DatabaseConfig.get_username()};"
        #         f"PWD={DatabaseConfig.get_password()};")

        #     return "mssql+pyodbc:///?odbc_connect={}".format(connection_attributes)

        # return f"postgresql+psycopg2://{connection}"
        
        return "sqlite:///test2.db"


class SQLClient:
    def __init__(self, url=ConnectionStringBuilder.get_default_connection_string()):
        try:
            engine = create_engine(url, echo=True)
            self.__session = sessionmaker(
                autocommit=False, autoflush=False, bind=engine)
        except Exception as e:
            raise

    
    def get_session(self):
        return self.__session()


sql_client = SQLClient()
