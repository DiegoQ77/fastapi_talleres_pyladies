from fastapi import APIRouter
from databases import Database

from app.services.product_service import ProductService 

router = APIRouter(prefix="/api/products", tags=["products"])

product_service = ProductService()

@router.get("/")
async def read_products():
    products = product_service.get_products()
    return products
