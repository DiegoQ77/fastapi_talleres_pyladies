from pydantic import BaseModel, condecimal

class ProductInput(BaseModel):
    name: str
    price: condecimal(max_digits=10, decimal_places=2)
    model: str
    category: str 
    stock: int 
    image: str 

class ProductOutput(BaseModel):
    id: int
    name: str
    price: condecimal(max_digits=10, decimal_places=2)
    model: str
    category: str 
    stock: int 
    image: str 
