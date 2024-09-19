from typing import TypeVar, Generic, Any
from uuid import UUID

from tortoise.queryset import QuerySet

T = TypeVar("T", bound="Model")


class BaseDAO(Generic[T]):
    _model: type[T]

    # def __init__(self, tmp_model: type[T]) -> None:
    #     super().__init__()
    #     self.tmp_model = tmp_model
    @classmethod
    def all(cls, skip: int = 0, limit: int | None = None) -> QuerySet:
        query: QuerySet = cls._model.all()
        if skip:
            query = query.offset(skip)
        if limit:
            query = query.limit(limit)
        return query

    @classmethod
    async def create(cls, *args: Any, **kwargs: Any) -> T:
        return await cls._model.create(*args, **kwargs)

    @classmethod
    async def update(cls, obj_id: UUID, return_obj: bool = False, **kwargs: Any) -> T | None:
        updated = await cls._model.select_for_update().filter(id=obj_id).update(**kwargs)
        if return_obj:
            return await cls.get(id=obj_id)
        return updated

    @classmethod
    async def delete(cls, *args: Any, **kwargs: Any) -> None:
        return await cls._model.delete(*args, **kwargs)

    @classmethod
    def filter(
        cls,
        *args: Any,
        skip: int = 0,
        limit: int | None = None,
        order_by: str | None = None,
        **kwargs: Any
    ) -> QuerySet[T]:
        query = cls.all(skip=skip, limit=limit)
        if kwargs or args:
            query = query.filter(*args, **kwargs)
        if order_by:
            query = query.order_by(order_by)
        return query

    @classmethod
    async def get(cls, *args: Any, **kwargs: Any) -> T:
        return await cls._model.filter(*args, **kwargs).get(*args, **kwargs)

    @classmethod
    async def get_or_none(cls, *args, **kwargs) -> T | None:
        return await cls._model.get_or_none(*args, **kwargs)


__all__ = [
    "BaseDAO",
    "T"
]
