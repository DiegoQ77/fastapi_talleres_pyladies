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
        
        
from fastapi import APIRouter, HTTPException
from databases import Database

from app.services.product_service import ProductService 
from app.domain.models import ProductInput

router = APIRouter(prefix="/api/products", tags=["products"])

@router.get("/")
async def read_products():
    products = product_service.get_products()
    return products




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
