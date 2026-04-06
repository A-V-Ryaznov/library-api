from pathlib import Path

from environs import Env

from .models import Config, WebConfig


def get_config(path: Path | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        web=WebConfig(
            port=env.int("WEB_PORT"),
            host=env.str("WEB_HOST"),
            base_url=env.str("WEB_BASE_URL")
        ),
    )
