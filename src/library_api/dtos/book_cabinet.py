from dataclasses import dataclass
from datetime import datetime

from library_api.custom_types import BookCabinetId, BookId, CabinetId


@dataclass(frozen=True, slots=True)
class BookCabinetDTO:
    id: BookCabinetId

    book_id: BookId
    cabinet_id: CabinetId
    is_exist: bool
    create_at: datetime


@dataclass(frozen=True, slots=True)
class NewBookCabinetDTO:
    book_id: BookId
    cabinet_id: CabinetId
    is_exist: bool
    create_at: datetime
