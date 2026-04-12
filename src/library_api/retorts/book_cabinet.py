from adaptix import name_mapping
from adaptix.conversion import allow_unlinked_optional, get_converter
from adaptix.type_tools import exec_type_checking

from library_api.db.models import book_cabinet
from library_api.dtos.book_cabinet import BookCabinetDTO, NewBookCabinetDTO

exec_type_checking(book_cabinet)

book_cabinet_cabinet_to_dto = get_converter(book_cabinet.BookCabinet, BookCabinetDTO)
new_book_cabinet_to_orm = get_converter(
    NewBookCabinetDTO,
    book_cabinet.BookCabinetId,
    recipe=[
        name_mapping(skip=["id", "update_at"]),
        allow_unlinked_optional()
    ],
)
