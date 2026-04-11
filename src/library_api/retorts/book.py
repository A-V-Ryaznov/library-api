from adaptix import name_mapping
from adaptix.conversion import allow_unlinked_optional, get_converter
from adaptix.type_tools import exec_type_checking

from library_api.dtos.book import BookDTO, NewBookDTO
from library_api.db.models import book

exec_type_checking(book)

book_to_dto = get_converter(book.Book, BookDTO)
new_book_to_orm = get_converter(
    NewBookDTO,
    book.Book,
    recipe=[
        name_mapping(skip=["id", "users", "cabinet"]),
        allow_unlinked_optional()
    ],
)