from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from library_api.custom_types import UserId
from library_api.db.models.user import User
from library_api.dtos.user import UserDTO
from library_api.exceptions.user import UserNotFound
from library_api.retorts.user import new_user_to_orm, user_to_dto


class UserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(self, dto: UserDTO) -> UserDTO:
        model = new_user_to_orm(dto)
        self._session.add(model)
        await self._session.flush([model])
        return user_to_dto(model)

    async def get_by_id(self, id: UserDTO) -> UserDTO:
        result = (
            await self._session.execute(
                select(UserId).where(User.id == id)
            )
        ).scalar()

        if result is None:
            raise UserNotFound
        return user_to_dto(result)

    async def get_all_users(self) -> list[UserDTO]:
        result = (
            await self._session.execute(
                select(User)
            )
        ).scalars().all()

        return [user_to_dto(user) for user in result]
