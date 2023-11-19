from app.repositories.sql_client import sql_client
from app.repositories.product_repository import ProductRepository


class ProductService:
    def __init__(self) -> None:
        self.__product_repository = ProductRepository()
        
    
    def get_products(self) -> None:
        try:
            programs_list = self.__product_repository.list()
            print("soy unit of work")
            print(programs_list[0].name)
            return None
        except Exception as e:
            raise  
        
    def get_product(self, id):
        pass 
    
    
    def update_product(self, id):
        pass  
    