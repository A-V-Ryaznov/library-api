from sqlalchemy import VARCHAR, BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from library_api.custom_types import OfficeId

from .base import Base


class Office(Base):
    __tablename__ = "offices"

    id: Mapped[OfficeId] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    adrres: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
