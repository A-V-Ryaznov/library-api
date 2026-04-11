from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class WebConfig:
    host: str = "127.0.0.1"
    port: int = 8282


@dataclass(frozen=True, slots=True)
class Config:
    web: WebConfig
