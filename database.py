import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load environment variables from .env file if it exists (for local development)
load_dotenv()

# Global variable to store the database client
mongodb_client = None
database = None

def get_database():
    """Get database connection, creating it if necessary"""
    global mongodb_client, database
    
    if mongodb_client is None or database is None:
        atlas_uri = os.getenv("ATLAS_URI")
        db_name = os.getenv("DB_NAME")
        
        if not atlas_uri:
            raise ValueError("ATLAS_URI environment variable is not set")
        
        if not db_name:
            raise ValueError("DB_NAME environment variable is not set")
        
        try:
            mongodb_client = MongoClient(atlas_uri)
            # Test the connection
            mongodb_client.admin.command('ping')
            database = mongodb_client[db_name]
        except Exception as e:
            raise RuntimeError(f"Failed to connect to MongoDB: {str(e)}")
    
    return database

def close_database_connection():
    """Close database connection"""
    global mongodb_client
    if mongodb_client:
        mongodb_client.close()
        mongodb_client = None