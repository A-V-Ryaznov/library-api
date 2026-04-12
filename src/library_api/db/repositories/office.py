from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from library_api.custom_types import OfficeId
from library_api.db.models.office import Office
from library_api.dtos.office import OfficeDTO, NewOfficeDTO
from library_api.exceptions.office import OfficeNotFound
from library_api.retorts.office import office_to_dto, new_office_to_orm

class UserRepository:
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
    
    async def get_all_offices(self) -> OfficeDTO:
        result = (
            await self._session.execute(
                select(Office)
            )
        ).scalars().all()

        if result is None:
            raise OfficeNotFound
        return office_to_dto(result)
