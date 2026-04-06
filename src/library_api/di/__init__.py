from typing import Any

from dishka import make_async_container, AsyncContainer

from library_api.config.models import Config, WebConfig
from .config import ConfigProvider
from .interactors import InteractorsProvider


def get_context(config: Config) -> dict[Any, Any]:
    return {
        Config: config,
        WebConfig: config.web,
    }


def create_container(config: Config) -> AsyncContainer:
    return make_async_container(
        ConfigProvider(),
        InteractorsProvider(),
        context=get_context(config)
    )


__all__ = [
    "create_container"
]