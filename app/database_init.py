from databases import Database

async def create_table(database):
    # Create a table.
    query = """CREATE TABLE Test (id INTEGER PRIMARY KEY, name VARCHAR(100), score INTEGER)"""
    await database.execute(query=query)

async def insert_data(database):
    query = "INSERT INTO Test(name, score) VALUES (:name, :score)"
    values = [
        {"name": "Daisy", "score": 92},
        {"name": "Neil", "score": 87},
        {"name": "Carol", "score": 43},
    ]
    await database.execute_many(query=query, values=values)

async def main():
    try:
        database = Database("sqlite:///pyladies.db")
        await database.connect()
        await create_table(database)
        await insert_data(database)
        query = "SELECT * FROM Test"
        results = await database.fetch_all(query=query)
        print("Existoso!")
        
    except Exception as e:
        raise e
        


# Run the event loop to execute the coroutine
import asyncio
asyncio.run(main())
