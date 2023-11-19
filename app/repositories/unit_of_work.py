import abc

from app.repositories.sql_client import sql_client
from app.repositories.product_repository import ProductRepository


class AbstractUnitOfWork(abc.ABC):
    @abc.abstractmethod
    def products(self):
        pass

class UnitOfWork(AbstractUnitOfWork):
    def __init__(self) -> None:
        self.__session = sql_client.get_session()
        self.__products_repo = None
        
    @property
    def products(self):
        if self.__products_repo is None:
            self.__products_repo = ProductRepository(self.__session)
        return self.__products_repo
