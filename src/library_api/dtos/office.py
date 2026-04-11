from dataclasses import dataclass

from library_api.custom_types import OfficeId


@dataclass(frozen=True, slots=True)
class OfficeDTO:
    id: OfficeId

    adrres: str


@dataclass(frozen=True, slots=True)
class NewOfficeDTO:
    adrres: str
