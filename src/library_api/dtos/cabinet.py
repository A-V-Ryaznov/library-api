from dataclasses import dataclass

from library_api.custom_types import OfficeId, UserId


@dataclass(frozen=True, slots=True)
class CabinetDTO:
    id: OfficeId

    name: str
    owner_id: UserId
    office_id: OfficeId
    number: str


@dataclass(frozen=True, slots=True)
class NewCabinetDTO:
    name: str
    owner_id: UserId
    office_id: OfficeId
    number: str
