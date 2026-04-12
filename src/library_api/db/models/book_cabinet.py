from datetime import datetime

from sqlalchemy import TIMESTAMP, BigInteger, Boolean, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from library_api.custom_types import BookCabinetId, BookId, CabinetId

from .base import Base


class BookCabinet(Base):
    __tablename__ = "book_cabinets"

    id: Mapped[BookCabinetId] = mapped_column(
        BigInteger, primary_key=True, autoincrement=True
    )
    book_id: Mapped[BookId] = mapped_column(BigInteger, ForeignKey("books.id"))
    cabinet_id: Mapped[CabinetId] = mapped_column(BigInteger, ForeignKey("cabinets.id"))
    is_exist: Mapped[bool] = mapped_column(Boolean, server_default="True", nullable=False)
    create_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), server_default=func.now(), nullable=False
    )
    update_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
