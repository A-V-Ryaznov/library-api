from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel, Field, field_validator
from datetime import date
from decimal import Decimal
import uvicorn

app = FastAPI()


"""
BOOKS
name
author
year
cost
"""

BOOKS = {
    "Pomadoro": ["Frank", 1990, 500.82],
    "Dune": ["Herbert", 1950, 300.64]
}

class BookRequests(BaseModel):
    name: str = Field(..., max_length=255)
    author: str = Field(..., max_length=255)
    year: int
    cost: Decimal = Field(max_digits=10, decimal_places=2)


    @field_validator("name")
    def book_name_not_empty(cls, v:str) -> str:
        v = v.strip()

        if not v:
            raise ValueError("Book name cannot be empty")
        
        return v


    @field_validator("cost")
    def cost_must_be_positive(cls, v: Decimal) -> Decimal:
        if v <= 0.0:
            raise ValueError("Cost must be positive")
        return v
        
    


# Get All books
@app.get("/health")
def health_check():
    return Response(status_code=200)

# Get All Books
@app.get("/books")
def get_books():
    return BOOKS

@app.get("/books/{name}")
def get_book(book: str | None = None):
    if book is None:
          raise HTTPException(
            status_code = 404,
            detail=f"Book_name is empty"
        )
    if book not in BOOKS:
        raise HTTPException(
            status_code = 404,
            detail=f"Book '{book}' not found"
        )
    
    return BOOKS[book]

@app.post("/book")
def create_book(book: BookRequests):
    if book.name in BOOKS:
        raise HTTPException(
            status_code=409,
            detail=f"Book '{book.name}' already exists"
        )

    BOOKS[book.name] = [book.author, book.year, book.cost]

    return { 
        "message": f"Book '{book.name}' was created",
        "book": book.name,
        "author": book.author,
        "year": book.year,
        "cost": book.cost
    }

