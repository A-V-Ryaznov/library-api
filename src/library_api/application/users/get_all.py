from library_api.db.repositories.user import UserRepository
from library_api.dtos.user import UserDTO


class GetAllUsersInteractor:
    def __init__(self, user_repostiory: UserRepository):
        self._user_repostiory = user_repostiory

    async def __call__(self) -> list[UserDTO]:
        users = await self._user_repostiory.get_all_users()

        return users