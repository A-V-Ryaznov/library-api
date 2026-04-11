from library_api.db.temp import books

from library_api.dtos.book import BookDTO, NewBookDTO
from library_api.helpers import generate_uuid
from library_api.types import BookId


class CreateNewBookInteractor:
    def __call__(self, data: NewBookDTO) -> None:
        book = BookDTO(
            id=BookId(generate_uuid()),
            name=data.name,
            author=data.author,
            year=data.year,
            cost=data.cost,
        )
        books[data.name] = book
        return book
