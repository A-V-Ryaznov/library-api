from dataclasses import dataclass

from library_api.custom_types import CabinetId, OfficeId, UserId


@dataclass(frozen=True, slots=True)
class CabinetDTO:
    id: CabinetId

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
