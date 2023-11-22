from app.data_access.models import Product
from app.repositories.sql_client import sql_client



class ProductRepository():
    def __init__(self, session=sql_client.get_session()):
        self.__session = session

    def list(self):
        try:
            products = self.__session.query(Product).all()
            return products
        except Exception as e:
            raise
    
    def get(self, id):
        try:
            # product = self.__session.query(Product).filter(Product.id == id).first()
            product = self.__session.get(Product, id)
            if product is None:
                return None
            return product
        except Exception as e:
            raise
        
    def add(self, product):
        try:
            product_base_model = Product(name=product.name, price=product.price, model=product.model, category=product.category, stock=product.stock, image=product.image)
            self.__session.add(product_base_model)
            self.__session.commit()
            self.__session.refresh(product_base_model)
            return product_base_model
            
        except Exception as e:
            raise 
        