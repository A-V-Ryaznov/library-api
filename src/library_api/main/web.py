import asyncio
import sys
import uvicorn

from contextlib import asynccontextmanager, suppress

from fastapi import FastAPI

from dishka import AsyncContainer
from dishka.integrations.fastapi import setup_dishka

from library_api.config.parsers import get_config
from library_api.di import create_container
from library_api.presentation.web.v1.routes import main_router


config = get_config()


@asynccontextmanager
async def lifespan(app: FastAPI):
    container: AsyncContainer = app.state.dishka_container
    yield
    await container.close()


def main() -> FastAPI:
    app = FastAPI(lifespan=lifespan)

    container = create_container(config)

    setup_dishka(
        container=container,
        app=app,
    )

    app.include_router(main_router)

    return app


def run() -> None:
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

    with suppress(KeyboardInterrupt):
        uvicorn.run(
            main(),
            host=config.web.host,
            port=config.web.port,
            proxy_headers=True,
            log_level="trace"
        )


if __name__ == "__main__":
    run()
