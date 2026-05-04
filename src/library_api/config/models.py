from dataclasses import dataclass
from pathlib import Path

from pydantic import PostgresDsn, SecretStr, BaseModel

BASE_DIR = Path(__file__).parent.parent


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



class AuthJWTConfig(BaseModel):
    private_key_path: Path = BASE_DIR / "security" /  "certs" / "jwt-private.pem"
    public_key_path: Path = BASE_DIR / "security" /  "certs" / "jwt-public.pem"
    algorithm: str = "RS256"

    # library-api/src/library_api/security/certs/jwt-private.pem    


@dataclass(frozen=True, slots=True)
class Config:
    web: WebConfig
    db: DatabaseConfig
    auth_jwt: AuthJWTConfig = AuthJWTConfig()

