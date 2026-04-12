from collections.abc import AsyncIterable

from dishka import AnyOf, Provider, Scope, provide, provide_all
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from library_api.config.models import DatabaseConfig
from library_api.db.repositories.book import BookRepository
from library_api.db.repositories.cabinet import CabinetRepository
from library_api.db.repositories.office import OfficeRepository
from library_api.db.repositories.user import UserRepository
from library_api.interface import DBSession


class DatabaseProvide(Provider):
    scope = Scope.APP

    @provide
    async def get_engine(self, config: DatabaseConfig) -> AsyncIterable[AsyncEngine]:
        engine = create_async_engine(config.make_url())
        yield engine
        await engine.dispose()

    @provide
    async def get_pool(self, engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(engine, expire_on_commit=False)

    @provide(scope=Scope.REQUEST)
    async def get_session(
        self, pool: async_sessionmaker[AsyncSession]
    ) -> AsyncIterable[AnyOf[AsyncSession, DBSession]]:
        async with pool() as session:
            yield session

    repositories = provide_all(
        BookRepository,
        CabinetRepository,
        OfficeRepository,
        UserRepository,
        scope=Scope.REQUEST
    )
