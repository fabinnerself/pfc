from fastapi import FastAPI
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from routes import router as book_router

# Load environment variables from .env file if it exists (for local development)
load_dotenv()

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    atlas_uri = os.getenv("ATLAS_URI")
    db_name = os.getenv("DB_NAME")
    app.mongodb_client = MongoClient(atlas_uri)
    app.database = app.mongodb_client[db_name]

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(book_router, tags=["books"], prefix="/book")
