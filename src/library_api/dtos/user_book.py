from dataclasses import dataclass
from datetime import datetime

from library_api.custom_types import BookId, UserBookId, UserId


@dataclass(frozen=True, slots=True)
class UserBookDTO:
    id: UserBookId

    book_id: BookId
    user_id: UserId
    borrowed_at: datetime
    returned_at: datetime | None
    is_returned: bool


@dataclass(frozen=True, slots=True)
class NewUserBookDTO:
    book_id: BookId
    user_id: UserId
    borrowed_at: datetime
    returned_at: datetime | None
    is_returned: bool
