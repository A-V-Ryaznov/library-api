from adaptix import name_mapping
from adaptix.conversion import allow_unlinked_optional, get_converter
from adaptix.type_tools import exec_type_checking

from library_api.db.models import user
from library_api.dtos.user import NewUserDTO, UserDTO

exec_type_checking(user)

user_to_dto = get_converter(user.User, UserDTO)
new_user_to_orm = get_converter(
    NewUserDTO,
    user.User,
    recipe=[
        name_mapping(skip=["id", "books"]),
        allow_unlinked_optional()
    ],
)
