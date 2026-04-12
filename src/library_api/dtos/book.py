from dataclasses import dataclass
from decimal import Decimal

from library_api.custom_types import BookId


@dataclass(frozen=True, slots=True)
class BookDTO:
    id: BookId

    name: str
    author: str
    year: str
    cost: Decimal
    tags: list[str] | None


@dataclass(frozen=True, slots=True)
class NewBookDTO:
    name: str
    author: str
    year: str
    cost: Decimal
    tags: list[str] | None
