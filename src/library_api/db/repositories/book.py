from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from library_api.custom_types import BookId
from library_api.db.models.book import Book
from library_api.dtos.book import BookDTO, NewBookDTO
from library_api.exceptions.book import BookNotFound
from library_api.retorts.book import new_book_to_orm, book_to_dto

class BookRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(self, dto: NewBookDTO) -> BookDTO:
        model = new_book_to_orm(dto)
        self._session.add(model)
        await self._session.flush([model])
        return book_to_dto(model)
    
    async def get_by_id(self, id: BookId) -> BookDTO:
        result = (
            await self._session.execute(
                select(Book).where(Book.id == id)
            )
        ).scalar()

        if result is None:
            raise BookNotFound
        return book_to_dto(result)
    
    async def get_all_books(self) -> BookDTO:
        result = (
            await self._session.execute(
                select(Book)
            )
        ).scalars().all()

        if result is None:
            raise BookNotFound
        return book_to_dto(result)
