from pydantic import BaseModel, Field

from app.db.models.events import EventState


class EventsFilter(BaseModel):
    state: EventState | None = None


__all__ = [
    "EventsFilter",
]
