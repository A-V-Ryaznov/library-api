from typing import TYPE_CHECKING

from sqlalchemy import VARCHAR, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from library_api.custom_types import OfficeId


from .base import Base

if TYPE_CHECKING:
    from library_api.db.models.cabinet import Cabinet

class Office(Base):
    __tablename__ = "offices"

    id: Mapped[OfficeId] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    adrres: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)

    cabinet: Mapped["Cabinet"] = relationship(
        "Cabinet", back_populates="office"
    )