from typing import Optional
from dataclasses import dataclass


@dataclass
class SecretCongig:
    jwt_secret: str
    manager_secret: str


@dataclass
class DatabaseConfig:
    username: str
    password: str
    host: str
    port: int
    name: str


@dataclass
class AppConfig:
    database: Optional[DatabaseConfig]
    secret: Optional[SecretCongig]
