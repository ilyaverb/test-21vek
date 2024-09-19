from app.config import settings

MODELS_MODULES: set[str] = {
    "app.db.models.events"
}

TORTOISE_CONFIG = {
    "connections": {
        "default": str(settings.db.uri)
    },
    "apps": {
        "models": {
            "models": list(MODELS_MODULES) + ["aerich.models"]
        }
    }
}

__all__ = [
    "TORTOISE_CONFIG",
]
