from app.repositories.repository import AbstractRepository
from app.data_access.models import Test


class ProductRepository(AbstractRepository):
    def __init__(self, session):
        self.__session = session

    def list(self):
        try:
            products = self.__session.query(Test).all()
            return products
        except Exception as e:

            raise