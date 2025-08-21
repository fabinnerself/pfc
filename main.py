from contextlib import asynccontextmanager
from fastapi import FastAPI
from routes import router as book_router
from database import get_database, close_database_connection

@asynccontextmanager
async def lifespan(app: FastAPI):
    get_database()
    yield
    close_database_connection()

app = FastAPI(lifespan=lifespan)

app.include_router(book_router, tags=["books"], prefix="/book")
