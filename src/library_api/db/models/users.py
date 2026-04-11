from datetime import datetime

from sqlalchemy import TIMESTAMP, VARCHAR, BigInteger, Boolean, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from library_api.custom_types import UserId
from library_api.db.models.books import Book

from .base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[UserId] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    firs_name: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    last_name: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    create_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), server_default=func.now(), nullable=False
    )
    is_admin: Mapped[bool] = mapped_column(
        Boolean, server_default="False", nullable=False
    )

    books: Mapped[list[Book]] = relationship(
        "Book", back_populates="users", secondary="user_books"
    )
