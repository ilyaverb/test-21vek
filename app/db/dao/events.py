from tortoise.queryset import QuerySet

from app.db.dao.base import BaseDAO, T
from app.db.models.events import EventModel, EventState


class EventsDAO(BaseDAO[EventModel]):
    _model = EventModel

    @classmethod
    def filter(cls, *args, state: EventState = None, **kwargs) -> QuerySet[T]:
        if state is None:
            return super().filter(*args, **kwargs)
        kwargs.update(state=state)
        return super().filter(*args, **kwargs)


__all__ = [
    "EventsDAO"
]
