from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from library_api.custom_types import CabinetId
from library_api.db.models.cabinet import Cabinet
from library_api.dtos.cabinet import CabinetDTO
from library_api.exceptions.cabinet import CabinetNotFound
from library_api.retorts.cabinet import cabinet_to_dto, new_cabinet_to_orm


class CabinetRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(self, dto: CabinetDTO) -> CabinetDTO:
        model = new_cabinet_to_orm(dto)
        self._session.add(model)
        await self._session.flush([model])
        return cabinet_to_dto(model)

    async def get_by_id(self, id: CabinetId) -> CabinetDTO:
        result = (
            await self._session.execute(
                select(CabinetId).where(Cabinet.id == id)
            )
        ).scalar()

        if result is None:
            raise CabinetNotFound
        return cabinet_to_dto(result)

    async def get_all_cabinet(self) -> list[CabinetDTO]:
        result = (
            await self._session.execute(
                select(CabinetDTO)
            )
        ).scalars().all()

        return [cabinet_to_dto(cabinet) for cabinet in result]
