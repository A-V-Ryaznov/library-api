from library_api.db.models.offices import Office
from library_api.db.models.users import User
from library_api.types import UserId, BookId, UserBookId
from datetime import datetime

from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BigInteger, ForeignKey, TIMESTAMP, func, Boolean

class UserBook(Base):
    __tablename__ = "user_books"

    id: Mapped[UserBookId] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    book_id: Mapped[BookId] = mapped_column(BigInteger, ForeignKey("book.id"))
    user_id: Mapped[UserId] = mapped_column(BigInteger, ForeignKey("users.id"))
    borrowed_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    returned_at: Mapped[datetime | None] = mapped_column(TIMESTAMP(timezone=True), nullable=True)
    is_returned: Mapped[bool] = mapped_column(Boolean, server_default="False", nullable=False)
