from dotenv import find_dotenv, load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

from app.config.db import DBSettings

load_dotenv(find_dotenv())

class AppSettings(BaseSettings):
    db: DBSettings = Field(default_factory=DBSettings)
    app_name: str | None = Field("", alias="APP_NAME")
    description: str | None = Field("", alias="DESCRIPTION")
    version: str | None = Field("0.0.1", alias="VERSION")


settings = AppSettings()

__all__ = [
    "AppSettings",
    "settings"
]