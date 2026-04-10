from library_api.types import OfficeId

from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger, VARCHAR


class Office(Base):
    __tablename__ = "offices"

    id: Mapped[OfficeId] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    adrres: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)