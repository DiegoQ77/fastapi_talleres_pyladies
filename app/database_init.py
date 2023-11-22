from databases import Database

import random
from datetime import datetime, timedelta

async def create_table(database):
    # Create a table.
    query = """
       
        CREATE TABLE Product (
            id INTEGER PRIMARY KEY,
            name VARCHAR(100),
            price DECIMAL(10, 2),  -- Cambiado a DECIMAL para almacenar precios con decimales
            model VARCHAR(50),      -- Cambiado a VARCHAR(50) para el modelo
            category VARCHAR(50),  -- Cambiado a VARCHAR(50) para la categoría
            stock INTEGER,
            image VARCHAR(255)    -- Cambiado a VARCHAR(255) para la ruta de la imagen
        );
        
    """
    await database.execute(query=query)

async def insert_data(database):
    query = """
        INSERT INTO Product(name, price, model, category, stock, image) 
        VALUES (:name, :price, :model, :category, :stock, :image)
    """
    
    # Lista de datos dummy para insertar
    car_models = ["Sedan", "SUV", "Truck", "Hatchback", "Convertible", "Coupe", "Minivan", "Pickup", "Crossover", "Sports Car"]
    
    
    product_data = [
        {"name": f"{random.choice(car_models)} 2000", "price": 29.99, "model": "ModelA", "category": "Category1", "stock": 50, "image": "image1.jpg"},
        {"name": f"{random.choice(car_models)} 2005", "price": 49.99, "model": "ModelB", "category": "Category2", "stock": 30, "image": "image2.jpg"},
        {"name": f"{random.choice(car_models)} 2010", "price": 39.99, "model": "ModelC", "category": "Category1", "stock": 20, "image": "image3.jpg"},
        {"name": f"{random.choice(car_models)} 2015", "price": 19.99, "model": "ModelA", "category": "Category3", "stock": 10, "image": "image4.jpg"},
        {"name": f"{random.choice(car_models)} 2020", "price": 59.99, "model": "ModelB", "category": "Category2", "stock": 40, "image": "image5.jpg"},
        {"name": f"{random.choice(car_models)} 2021", "price": 34.99, "model": "ModelC", "category": "Category1", "stock": 15, "image": "image6.jpg"},
        {"name": f"{random.choice(car_models)} 2018", "price": 24.99, "model": "ModelA", "category": "Category3", "stock": 25, "image": "image7.jpg"},
        {"name": f"{random.choice(car_models)} 2019", "price": 44.99, "model": "ModelB", "category": "Category2", "stock": 35, "image": "image8.jpg"},
        {"name": f"{random.choice(car_models)} 2022", "price": 54.99, "model": "ModelC", "category": "Category1", "stock": 45, "image": "image9.jpg"},
        {"name": f"{random.choice(car_models)} 2017", "price": 29.99, "model": "ModelA", "category": "Category3", "stock": 50, "image": "image10.jpg"},
    ]
    
    await database.execute_many(query=query, values=product_data)

async def main():
    try:
        database = Database("sqlite:///pyladies.db")
        await database.connect()
        await create_table(database)
        await insert_data(database)
        query = "SELECT * FROM Product"
        results = await database.fetch_all(query=query)
        print("Existoso!")
        
    except Exception as e:
        raise e
        


# Run the event loop to execute the coroutine
import asyncio
asyncio.run(main())
