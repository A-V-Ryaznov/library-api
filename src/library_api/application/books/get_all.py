from library_api.db.repositories.book import BookRepository
from library_api.dtos.book import BookDTO


class GetAllBooksInteractor:
    def __init__(self, books_repostiory: BookRepository):
        self._books_repostiory = books_repostiory

    async def __call__(self) -> list[BookDTO]:
        books = await self._books_repostiory.get_all_books()

        return books
