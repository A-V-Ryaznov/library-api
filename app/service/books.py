from fastapi import FastAPI, HTTPException
from fastapi.responses import Response

from app.schemas.book_shema import BookRequests
from app.repository import books as books_repository


def get_all_books():
    return books_repository.get_all_books()


def get_book(book_name: str | None = None):
    if book_name is None:
          raise HTTPException(
            status_code = 404,
            detail=f"Book_name is empty"
        )
    if not books_repository.is_book_exist(book_name):
        raise HTTPException(
            status_code = 404,
            detail=f"Book '{book_name}' not found"
        )
    
def create_book(book: BookRequests):
    if books_repository.is_book_exist(book.name):
        raise HTTPException(
            status_code=409,
            detail=f"Book '{book.name}' already exists"
        )

    books_repository.add_book(book.name, book.author, book.year, book.cost)

    return { 
        "message": f"Book '{book.name}' was created",
        "book": book.name,
        "author": book.author,
        "year": book.year,
        "cost": book.cost
    }