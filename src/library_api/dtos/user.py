from dataclasses import dataclass
from datetime import datetime

from library_api.custom_types import UserId


@dataclass(frozen=True, slots=True)
class UserDTO:
    id: UserId

    firs_name: str
    last_name: str
    email: str
    password: str
    is_admin: bool
    create_at: datetime


@dataclass(frozen=True, slots=True)
class NewUserDTO:
    firs_name: str
    last_name: str
    email: str
    password: str
    is_admin: bool
