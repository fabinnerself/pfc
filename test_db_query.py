from dotenv import dotenv_values
from pymongo import MongoClient

# Cargar las variables de entorno
config = dotenv_values(".env")

# Intentar conectar a la base de datos
try:
    client = MongoClient(config["ATLAS_URI"])
    db = client[config["DB_NAME"]]
    
    # Intentar listar las colecciones para verificar la conexión
    collections = db.list_collection_names()
    print("Conexión exitosa a la base de datos")
    print(f"Colecciones disponibles: {collections}")
    
    # Intentar consultar los libros
    books_collection = db["books"]
    books = list(books_collection.find(limit=100))
    print(f"Libros encontrados: {len(books)}")
    for book in books:
        print(book)
    
    # Cerrar la conexión
    client.close()
    
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")