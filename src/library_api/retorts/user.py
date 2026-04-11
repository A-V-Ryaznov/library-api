from adaptix import name_mapping
from adaptix.conversion import allow_unlinked_optional, get_converter
from adaptix.type_tools import exec_type_checking

from library_api.dtos.user import UserDTO, NewUserDTO
from library_api.db.models import user

exec_type_checking(user)

book_to_dto = get_converter(user.User, UserDTO)
new_book_to_orm = get_converter(
    NewUserDTO,
    user.User,
    recipe=[
        name_mapping(skip=["id", "books"]),
        allow_unlinked_optional()
    ],
)