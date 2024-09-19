from typing import Generic, TypeVar

from pydantic import BaseModel, Field
from tortoise.queryset import QuerySet


T = TypeVar("T", bound="PydanticModel")


class PaginatedRequest(BaseModel):
    skip: int | None = Field(default=0)
    limit: int | None = Field(default=25)


class PaginatedResponse(BaseModel, Generic[T]):
    count: int
    results: list[T]

    @classmethod
    async def resolve_pagination(
        cls,
        queryset: QuerySet,
        schema: type[T],
        skip: int = 0,
        limit: int = None,
    ) -> "PaginatedResponse[T] | list[T]":
        if limit:
            count = await queryset.count()
            results = await schema.from_queryset(queryset.offset(skip).limit(limit))
            return PaginatedResponse[schema](
                count=count,
                results=results
            )
        return await schema.from_queryset(queryset)


__all__ = [
    "PaginatedRequest",
    "PaginatedResponse"
]
