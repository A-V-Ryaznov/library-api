from adaptix import name_mapping
from adaptix.conversion import allow_unlinked_optional, get_converter
from adaptix.type_tools import exec_type_checking

from library_api.db.models import office
from library_api.dtos.office import NewOfficeDTO, OfficeDTO

exec_type_checking(office)

office_to_dto = get_converter(office.Office, OfficeDTO)
new_office_to_orm = get_converter(
    NewOfficeDTO,
    office.Cabinet,
    recipe=[
        name_mapping(skip=["id"]),
        allow_unlinked_optional()
    ],
)
