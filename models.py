import uuid
from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

class Book(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    author: str = Field(...)
    price: float = Field(...)
    description: str = Field(...)
    created_at: str = Field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = Field(default_factory=lambda: datetime.now().isoformat())

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "68a13535fb44e20903a1eeaf",
                "name": "book2",
                "author": "autor1",
                "price": 1.0,
                "description": "string",
                "created_at": "2025-08-20T19:24:00.000000",
                "updated_at": "2025-08-20T19:24:00.000000"
            }
        }


class BookUpdate(Book):
    name: Optional[str] = None
    author: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "book2",
                "author": "autor1",
                "price": 1.0,
                "description": "string",
                "created_at": "2025-08-20T19:24:00.000000",
                "updated_at": "2025-08-20T19:24:00.000000"
            }
        }
