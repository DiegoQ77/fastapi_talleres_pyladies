from typing import Union
from app.routes import products
from databases import Database

from fastapi import FastAPI



app = FastAPI()



app.include_router(products.router)


