from adaptix import name_mapping
from adaptix.conversion import allow_unlinked_optional, get_converter
from adaptix.type_tools import exec_type_checking

from library_api.dtos.user_book import UserBookDTO, NewUserBookDTO
from library_api.db.models import user_book

exec_type_checking(user_book)

book_to_dto = get_converter(user_book.UserBook, UserBookDTO)
new_book_to_orm = get_converter(
    NewUserBookDTO,
    user_book.UserBook,
    recipe=[
        name_mapping(skip=["id"]),
        allow_unlinked_optional()
    ],
)