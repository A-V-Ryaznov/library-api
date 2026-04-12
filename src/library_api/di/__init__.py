from typing import Any

from dishka import AsyncContainer, make_async_container

from library_api.config.models import Config, DatabaseConfig, WebConfig
from library_api.di.db import DatabaseProvide

from .config import ConfigProvider
from .interactors import InteractorsProvider


def get_context(config: Config) -> dict[Any, Any]:
    return {
        Config: config,
        WebConfig: config.web,
        DatabaseConfig: config.db
    }


def create_container(config: Config) -> AsyncContainer:
    return make_async_container(
        ConfigProvider(), DatabaseProvide(), InteractorsProvider(), context=get_context(config)
    )


__all__ = ["create_container"]
