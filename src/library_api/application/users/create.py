from library_api.db.repositories.user import UserRepository
from library_api.dtos.user import UserDTO, NewUserDTO
from library_api.interface import DBSession


class CreateNewUserInteractor:
    def __init__(self, user_repostiory: UserRepository, session: DBSession):
        self._user_repostiory = user_repostiory
        self._session = session

    async def __call__(self, data: NewUserDTO) -> UserDTO:
        user = await self._user_repostiory.create(data)
        await self._session.commit()

        return user
