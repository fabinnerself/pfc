from dotenv import dotenv_values
from pymongo import MongoClient
from routes import list_books
from fastapi import Request
import asyncio

# Crear una clase de solicitud simulada
class MockRequest:
    def __init__(self, db):
        self.app = type('App', (), {'database': db})()

# Cargar las variables de entorno
config = dotenv_values(".env")

# Conectar a la base de datos
client = MongoClient(config["ATLAS_URI"])
db = client[config["DB_NAME"]]

# Crear una solicitud simulada
request = MockRequest(db)

# Llamar a la función list_books
try:
    books = list_books(request)
    print(f"Libros encontrados: {len(books)}")
    for book in books:
        print(book)
except Exception as e:
    print(f"Error: {e}")

# Cerrar la conexión
client.close()