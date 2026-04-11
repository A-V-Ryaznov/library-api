from datetime import datetime

from sqlalchemy import TIMESTAMP, BigInteger, Boolean, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from library_api.custom_types import BookId, UserBookId, UserId

from .base import Base


class UserBook(Base):
    __tablename__ = "user_books"

    id: Mapped[UserBookId] = mapped_column(
        BigInteger, primary_key=True, autoincrement=True
    )
    book_id: Mapped[BookId] = mapped_column(BigInteger, ForeignKey("book.id"))
    user_id: Mapped[UserId] = mapped_column(BigInteger, ForeignKey("users.id"))
    borrowed_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), server_default=func.now(), nullable=False
    )
    returned_at: Mapped[datetime | None] = mapped_column(
        TIMESTAMP(timezone=True), nullable=True
    )
    is_returned: Mapped[bool] = mapped_column(
        Boolean, server_default="False", nullable=False
    )
