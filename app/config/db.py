from pydantic import Field, PostgresDsn
from typing import Annotated
from pydantic.networks import UrlConstraints
from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseSettings):
    uri: Annotated[
        PostgresDsn,
        UrlConstraints(
            allowed_schemes=[
                "postgresql+asyncpg",
                "postgresql+pg8000",
                "asyncpg"
            ]
        )
    ] = Field(..., alias="DATABASE_URL")


__all__ = [
    "DBSettings"
]
