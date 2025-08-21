from fastapi import FastAPI
from routes import router as book_router
from database import get_database, close_database_connection

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    """Initialize database connection on startup"""
    get_database()

@app.on_event("shutdown")
def shutdown_db_client():
    """Close database connection on shutdown"""
    close_database_connection()

app.include_router(book_router, tags=["books"], prefix="/book")
