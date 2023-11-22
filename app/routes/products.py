from fastapi import APIRouter, HTTPException
from databases import Database

from app.services.product_service import ProductService 
from app.domain.models import ProductInput

router = APIRouter(prefix="/api/products", tags=["products"])

product_service = ProductService()

@router.get("/")
async def read_products():
    products = product_service.get_products()
    return products


@router.get("/{id}")
async def get_product(id):
    product = product_service.get_product(id)
    if product is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return product


@router.post("/")
async def add_product(product:ProductInput):
    product = product_service.add_product(product)
    return product
