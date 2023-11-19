from fastapi import APIRouter
from databases import Database

from app.services.product_service import ProductService 

product_service = ProductService()


router = APIRouter(prefix="/api/products", tags=["products"])


@router.get("/")
async def read_products():
    products = product_service.get_products()
    return products
