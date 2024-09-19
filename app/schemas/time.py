from datetime import datetime

from pydantic import BaseModel


class TimestampMixin(BaseModel):
    created_at: datetime | None
    modified_at: datetime | None


__all__ = [
    "TimestampMixin",
]
