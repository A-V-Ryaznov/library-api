from .base import AppException


class BooksException(AppException):
    pass


class BookNotFound(BooksException):
    message = "Book not found"


class BookAlreadyExists(BooksException):
    message = "This book already exists"
