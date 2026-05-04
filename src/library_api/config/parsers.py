from pathlib import Path

from environs import Env
from pydantic import SecretStr

from .models import Config, DatabaseConfig, WebConfig

 
def get_config(path: Path | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        web=WebConfig(
            port=env.int("WEB_PORT"),
            host=env.str("WEB_HOST"),
        ),
        db=DatabaseConfig(
            path=env.str("POSTGRES_PATH"),
            username=env.str("POSTGRES_USER"),
            password=SecretStr(env.str("POSTGRES_USER")),
            host=env.str("POSTGRES_HOST"),
            port=env.int("POSTGRES_PORT"),
            scheme=env.str("POSTGRES_SCHEME")
        )
    )
