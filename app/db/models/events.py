import enum
from uuid import uuid4

from tortoise import Model, fields

from app.db.models.mixins.time import TimeStampMixin


class EventState(str, enum.Enum):
    NEW = "new"
    FINISHED_WIN = "finished_win"
    FINISHED_LOSE = "finished_lose"


class EventModel(TimeStampMixin):
    id = fields.UUIDField(default=uuid4, pk=True)
    coefficient = fields.DecimalField(max_digits=4, decimal_places=2)
    deadline = fields.DatetimeField()
    state = fields.CharEnumField(enum_type=EventState, null=False, max_length=13)


__all__ = [
    "EventState",
    "EventModel",
]