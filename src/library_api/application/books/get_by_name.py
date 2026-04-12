from library_api.db.repositories.book import BookRepository
from library_api.dtos.book import BookDTO


class GetBookByNameInteractor:
    def __init__(self, books_repostiory: BookRepository):
        self._books_repostiory = books_repostiory

    async def __call__(self, name: str) -> BookDTO:
        book = await self._books_repostiory.get_by_name(name)

        return book
