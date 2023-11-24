from typing import Union
from app.routes import products
from databases import Database

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI



app = FastAPI()

origins = [
    "http://localhost:5173/",
    "http://localhost:5173/*",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(products.router)


