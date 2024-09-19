from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.api import api_router
from app.config.default import settings
from app.db.config import TORTOISE_CONFIG
from app.middleware.errors import set_errors

app = FastAPI(
    title=settings.app_name,
    description=settings.description,
    version=settings.version,
)

set_errors(app)

register_tortoise(app, config=TORTOISE_CONFIG)

app.include_router(api_router)


__all__ = [
    "app"
]
