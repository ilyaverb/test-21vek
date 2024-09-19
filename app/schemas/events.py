from decimal import Decimal
from datetime import datetime

from pydantic import UUID4, ConfigDict, Field
from tortoise.contrib.pydantic.base import PydanticModel

from app.db.models.events import EventState, EventModel


class EventInputDTO(PydanticModel):
    model_config = ConfigDict(orig_model=EventModel, use_enum_values=True)
    coefficient: Decimal
    deadline: datetime
    state: EventState = Field(default=EventState.NEW)


class EventOutputDTO(EventInputDTO):
    id: UUID4


__all__ = [
    "EventInputDTO",
    "EventOutputDTO",
]
