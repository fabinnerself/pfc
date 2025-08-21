from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.testclient import TestClient
from dotenv import dotenv_values
from pymongo import MongoClient
from routes import router as book_router

config = dotenv_values(".env")

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"] + "test"]
    print("startup")
    yield
    print("shutdown")
    app.mongodb_client.close()

app = FastAPI(lifespan=lifespan)
app.include_router(book_router, tags=["books"], prefix="/book")


def test_create_book():
    with TestClient(app) as client:
        response = client.post("/book/", json={"name": "Don Quixote", "author": "Miguel de Cervantes", "price": 19.99, "description": "..."})
        assert response.status_code == 201

        body = response.json()
        assert body.get("name") == "Don Quixote"
        assert body.get("author") == "Miguel de Cervantes"
        assert body.get("price") == 19.99
        assert body.get("description") == "..."
        assert "_id" in body
        assert "created_at" in body
        assert "updated_at" in body


def test_create_book_missing_name():
    with TestClient(app) as client:
        response = client.post("/book/", json={"author": "Miguel de Cervantes", "price": 19.99, "description": "..."})
        assert response.status_code == 422


def test_create_book_missing_author():
    with TestClient(app) as client:
        response = client.post("/book/", json={"name": "Don Quixote", "price": 19.99, "description": "..."})
        assert response.status_code == 422


def test_create_book_missing_price():
    with TestClient(app) as client:
        response = client.post("/book/", json={"name": "Don Quixote", "author": "Miguel de Cervantes", "description": "..."})
        assert response.status_code == 422


def test_get_book():
    with TestClient(app) as client:
        new_book = client.post("/book/", json={"name": "Don Quixote", "author": "Miguel de Cervantes", "price": 19.99, "description": "..."}).json()

        get_book_response = client.get("/book/" + new_book.get("_id"))
        assert get_book_response.status_code == 200
        assert get_book_response.json() == new_book


def test_get_book_unexisting():
    with TestClient(app) as client:
        # Using a valid ObjectId format that doesn't exist in the database
        get_book_response = client.get("/book/507f1f77bcf86cd799439011")
        assert get_book_response.status_code == 404


def test_update_book():
    with TestClient(app) as client:
        new_book = client.post("/book/", json={"name": "Don Quixote", "author": "Miguel de Cervantes", "price": 19.99, "description": "..."}).json()

        response = client.put("/book/" + new_book.get("_id"), json={"name": "Don Quixote 1"})
        assert response.status_code == 200
        assert response.json().get("name") == "Don Quixote 1"


def test_update_book_unexisting():
    with TestClient(app) as client:
        # Then try to update a non-existent book
        update_book_response = client.put("/book/507f1f77bcf86cd79943901", json={"name": "Don Quixote 1"})
        assert update_book_response.status_code == 404


def test_delete_book():
    with TestClient(app) as client:
        new_book = client.post("/book/", json={"name": "Don Quixote", "author": "Miguel de Cervantes", "price": 19.99, "description": "..."}).json()

        delete_book_response = client.delete("/book/" + new_book.get("_id"))
        assert delete_book_response.status_code == 204


def test_delete_book_unexisting():
    with TestClient(app) as client:
        delete_book_response = client.delete("/book/507f1f77bcf86cd799439011")
        assert delete_book_response.status_code == 404

