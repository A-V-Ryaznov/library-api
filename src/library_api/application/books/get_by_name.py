from library_api.db.temp import books

from library_api.dtos.book import BookDTO
from library_api.exceptions.book import BookNotFound


class GetBookByNameInteractor:
    def __call__(self, name: str) -> BookDTO:
        if book := books.get(name, None):
            return book
        raise BookNotFound
