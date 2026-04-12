from adaptix import name_mapping
from adaptix.conversion import allow_unlinked_optional, get_converter
from adaptix.type_tools import exec_type_checking

from library_api.dtos.cabinet import CabinetDTO, NewCabinetDTO
from library_api.db.models import cabinet

exec_type_checking(cabinet)

cabinet_to_dto = get_converter(cabinet.Cabinet, CabinetDTO)
new_cabinet_to_orm = get_converter(
    NewCabinetDTO,
    cabinet.Cabinet,
    recipe=[
        name_mapping(skip=["id", "user", "office", "books"]),
        allow_unlinked_optional()
    ],
)