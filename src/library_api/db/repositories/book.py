from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

import logging

from library_api.db.models.book import Book
from library_api.dtos.book import BookDTO, NewBookDTO
from library_api.exceptions.book import BookNotFound
from library_api.retorts.book import book_to_dto, new_book_to_orm

logger = logging.getLogger(__name__)

class BookRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(self, dto: NewBookDTO) -> BookDTO:
        model = new_book_to_orm(dto)
        self._session.add(model)
        await self._session.flush([model])
        return book_to_dto(model)

    async def get_by_name(self, name: str) -> BookDTO:
        result = (
            await self._session.execute(
                select(Book).where(Book.name == name)
            )
        ).scalar()

        if result is None:
            raise BookNotFound
        

        return book_to_dto(result)

    async def get_all_books(self) -> list[BookDTO]:
        result = (
            await self._session.execute(
                select(Book)
            )
        ).scalars().all()

        return [book_to_dto(book) for book in result]
