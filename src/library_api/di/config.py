from dishka import Provider, Scope, from_context

from library_api.config.models import (
    Config,
    WebConfig
)


class ConfigProvider(Provider):
    scope = Scope.APP

    configs = (
        from_context(Config)
        + from_context(WebConfig)
    )
