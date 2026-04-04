from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel
from datetime import date
import uvicorn

app = FastAPI()


"""
BOOKS

name
author
year
create_at 
warranty
borrowed_at

"""

BOOKS = {
    "Pomadoro": ["Frank", "1990"],
    "Dune": ["Herbert", "1950"]
}

class OperationRequests(BaseModel):
    book_name: str
    author: str
    year: str


@app.get("/health")
def health_check():
    return Response(status_code=200)

@app.get("/books")
def get_books():
    return BOOKS


@app.get("/books/{name}")
def get_book(book_name: str | None = None):
    if book_name is None:
          raise HTTPException(
            status_code = 404,
            detail=f"Book_name is empty"
        )
    if book_name not in BOOKS:
        raise HTTPException(
            status_code = 404,
            detail=f"Book '{book_name}' not found"
        )
    
    return BOOKS[book_name]

@app.post("/book/{name}")
def create_book(name: str, author: str, year: str):
    if name in BOOKS:
        raise HTTPException(
            status_code=409,
            detail=f"Book '{name}' already exists"
        )

    BOOKS[name] = [author, year]
    #BOOKS[name] = initial_book

    return {
        "message": f"Book '{name}' was created",
        "book": name,
        "author": author,
        "year": year
    }

