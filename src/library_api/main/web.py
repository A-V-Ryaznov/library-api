import asyncio
import sys
from contextlib import asynccontextmanager, suppress

import uvicorn
from dishka import AsyncContainer
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from library_api.config.parsers import get_config
from library_api.di import create_container
from library_api.presentation.web.v1.routes import main_router

import logging.config
import yaml

config = get_config()

with open("logging_config.yaml", "rt") as f:
    log_config = yaml.safe_load(f.read())

logging.config.dictConfig(log_config)


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
            log_level="trace",
        )


if __name__ == "__main__":
    run()
