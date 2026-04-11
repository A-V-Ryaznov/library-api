from decimal import Decimal

from sqlalchemy import DECIMAL, JSON, VARCHAR, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from library_api.db.models.cabinets import Cabinet
from library_api.db.models.users import User
from library_api.types import BookId

from .base import Base


class Book(Base):
    __table__ = "books"

    id: Mapped[BookId] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    author: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    year: Mapped[str] = mapped_column(VARCHAR(4), nullable=False)
    cost: Mapped[Decimal] = mapped_column(DECIMAL(10, 2), nullable=False)
    tags: Mapped[list[str] | None] = mapped_column(JSON, nullable=True)

    users: Mapped[list[User]] = relationship(
        "User", back_populates="books", secondary="user_books"
    )

    cabinet: Mapped[list[Cabinet]] = relationship(
        "Cabinet", back_populates="cabinets", secondary="book_cabinets"
    )
