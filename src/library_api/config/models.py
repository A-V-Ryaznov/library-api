from dataclasses import dataclass

from pydantic import PostgresDsn, SecretStr


@dataclass(frozen=True, slots=True)
class DatabaseConfig:
    host: str
    port: int
    username: str
    path: str

    password: SecretStr
    scheme: str = "postgresql+asyncpg"

    def make_url(self) -> str:
        dsn: PostgresDsn = PostgresDsn.build(
            scheme=self.scheme,
            username=self.username,
            password=self.password.get_secret_value(),
            host=self.host,
            port=self.port,
            path=self.path,
        )
        return dsn.encoded_string()


@dataclass(frozen=True, slots=True)
class WebConfig:
    host: str = "127.0.0.1"
    port: int = 8282


@dataclass(frozen=True, slots=True)
class Config:
    web: WebConfig
    db: DatabaseConfig
