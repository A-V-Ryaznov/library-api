from fastapi import APIRouter
from fastapi.responses import Response

from app.schemas.book_shema import BookRequests
from app.service import books as books_service

router = APIRouter()

# Get All books
@router.get("/health")
def health_check():
    return Response(status_code=200)

# Get All Books
@router.get("/books")
def get_all_books():
    return books_service.get_all_books()

@router.get("/books/{name}")
def get_book(name: str | None = None):
    return books_service.get_book(name)

@router.post("/book")
def create_book(book: BookRequests):
    return books_service.create_book(book)