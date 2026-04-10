from library_api.db.models.users import User
from library_api.types import CabinetId, UserId, OfficeId

from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BigInteger, VARCHAR, ForeignKey


class Cabinet(Base):
    __tablename__ = "cabinets"

    id: Mapped[CabinetId] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id"))
    office_id: Mapped[OfficeId] = mapped_column(BigInteger, ForeignKey("offices.id"))


    user: Mapped[User] = relationship(
        "User",
        back_populates="cabinet",
        foreign_keys=[user_id]
    )