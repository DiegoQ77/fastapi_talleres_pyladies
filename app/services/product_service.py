from app.repositories.sql_client import sql_client
from app.repositories.product_repository import ProductRepository
from app.domain.models import ProductOutput


class ProductService:
    def __init__(self) -> None:
        self.__product_repository = ProductRepository()
        
    
    def get_products(self) -> None:
        try:
            programs_list = self.__product_repository.list()
            products_output = [ ProductOutput(
                                    id=product.id,
                                    name=product.name, 
                                    price=product.price, 
                                    model=product.model, 
                                    category=product.category, 
                                    stock=product.stock, 
                                    image=product.image) 
                               for product in programs_list]
            return products_output
        except Exception as e:
            raise  
        
        
    def get_product(self, id):
        product = self.__product_repository.get(id)
        if product is None:
            return None
        
        product_output = ProductOutput(
                                    id=product.id,
                                    name=product.name, 
                                    price=product.price, 
                                    model=product.model, 
                                    category=product.category, 
                                    stock=product.stock, 
                                    image=product.image
                        ) 
        return product_output
 
    
    def add_product(self, product):
        product = self.__product_repository.add(product)
        product_output = ProductOutput(
                            id=product.id,
                            name=product.name, 
                            price=product.price, 
                            model=product.model, 
                            category=product.category, 
                            stock=product.stock, 
                            image=product.image
                ) 
        return product_output
  
    