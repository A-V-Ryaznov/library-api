from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from library_api.custom_types import OfficeId
from library_api.db.models.office import Office
from library_api.dtos.office import OfficeDTO
from library_api.exceptions.office import OfficeNotFound
from library_api.retorts.office import new_office_to_orm, office_to_dto


class OfficeRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(self, dto: OfficeDTO) -> OfficeDTO:
        model = new_office_to_orm(dto)
        self._session.add(model)
        await self._session.flush([model])
        return office_to_dto(model)

    async def get_by_id(self, id: OfficeDTO) -> OfficeDTO:
        result = (
            await self._session.execute(
                select(OfficeId).where(Office.id == id)
            )
        ).scalar()

        if result is None:
            raise OfficeNotFound
        return office_to_dto(result)

    async def get_all_offices(self) -> list[OfficeDTO]:
        result = (
            await self._session.execute(
                select(Office)
            )
        ).scalars().all()

        return [office_to_dto(office) for office in result]
