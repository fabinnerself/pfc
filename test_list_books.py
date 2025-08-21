from contextlib import asynccontextmanager
from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from routes import router as book_router

config = dotenv_values(".env")

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("startup")
    yield
    print("shutdown")
    app.mongodb_client.close()

app = FastAPI(lifespan=lifespan)

app.include_router(book_router, tags=["books"], prefix="/book")

# Función para probar la ruta de listado de libros
def test_list_books():
    import requests
    try:
        response = requests.get("http://localhost:8000/book/")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_list_books()