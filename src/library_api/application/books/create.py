from library_api.db.repositories.book import BookRepository
from library_api.dtos.book import BookDTO, NewBookDTO
from library_api.interface import DBSession


class CreateNewBookInteractor:
    def __init__(self, books_repostiory: BookRepository, session: DBSession):
        self._books_repostiory = books_repostiory
        self._session = session

    async def __call__(self, data: NewBookDTO) -> BookDTO:
        book = await self._books_repostiory.create(data)
        await self._session.commit()

        return book
