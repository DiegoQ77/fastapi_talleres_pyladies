from app.data_access.models import Test
from app.repositories.sql_client import sql_client



class ProductRepository():
    def __init__(self, session=sql_client.get_session()):
        self.__session = session

    def list(self):
        try:
            products = self.__session.query(Test).all()
            return products
        except Exception as e:

            raise