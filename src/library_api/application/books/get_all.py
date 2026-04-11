from library_api.db.temp import books
from library_api.dtos.book import BookDTO


class GetAllBooksInteractor:
    def __call__(self) -> tuple[BookDTO]:
        return tuple(books.values())
