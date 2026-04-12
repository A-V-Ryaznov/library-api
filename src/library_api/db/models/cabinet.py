from sqlalchemy import VARCHAR, BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from library_api.custom_types import CabinetId, OfficeId, UserId


from .base import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from library_api.db.models.book import Book
    from library_api.db.models.office import Office
    from library_api.db.models.user import User

class Cabinet(Base):
    __tablename__ = "cabinets"

    id: Mapped[CabinetId] = mapped_column(
        BigInteger, primary_key=True, autoincrement=True
    )
    name: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    owner_id: Mapped[UserId] = mapped_column(BigInteger, ForeignKey("users.id"))
    office_id: Mapped[OfficeId] = mapped_column(BigInteger, ForeignKey("offices.id"))
    number: Mapped[str] = mapped_column(VARCHAR(10))

    user: Mapped["User"] = relationship(
        "User", back_populates="cabinet", foreign_keys=[owner_id]
    )

    office: Mapped["Office"] = relationship(
        "Office", back_populates="cabinets", foreign_keys=[office_id]
    )

    books: Mapped["list[Book]"] = relationship(
        "Book", back_populates="cabinets", secondary="book_cabinets"
    )
