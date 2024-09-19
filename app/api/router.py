from fastapi import APIRouter

from app.api.events import router as events_router
from app.api.healthcheck import router as healthcheck_router

api_router = APIRouter()

api_router.include_router(healthcheck_router)
api_router.include_router(events_router)

__all__ = [
    "api_router"
]
