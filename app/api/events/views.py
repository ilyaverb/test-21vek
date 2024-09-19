from fastapi import APIRouter, Body, Depends, Request
from pydantic import UUID4
from starlette import status
from starlette.status import HTTP_204_NO_CONTENT
from tortoise.queryset import QuerySet
from tortoise.transactions import atomic

from app.db.dao.events import EventsDAO
from app.filters.events import EventsFilter
from app.schemas.events import EventOutputDTO, EventInputDTO
from app.schemas.pagination import PaginatedRequest, PaginatedResponse

router = APIRouter(prefix="/events", tags=["events"])


@router.get("/", response_model=PaginatedResponse[EventOutputDTO], status_code=status.HTTP_200_OK)
async def get_all(
    filter_schema: EventsFilter = Depends(),
    pagination: PaginatedRequest = Depends(),
) -> list[EventOutputDTO]:
    events_qs: QuerySet = EventsDAO.filter(**filter_schema.model_dump())

    return await PaginatedResponse.resolve_pagination(
        queryset=events_qs,
        schema=EventOutputDTO,
        skip=pagination.skip,
        limit=pagination.limit
    )


@router.get("/{id:uuid}/")
async def get(
    id: UUID4
) -> EventOutputDTO:
    event = await EventsDAO.get(id=id)
    return await EventOutputDTO.from_tortoise_orm(event)


@router.post("/")
@atomic()
async def create(
    request: Request,
    schema: EventInputDTO
) -> EventOutputDTO:
    obj = await EventsDAO.create(**schema.model_dump())
    return await EventOutputDTO.from_tortoise_orm(obj)


@router.delete("/{id:uuid}/", status_code=HTTP_204_NO_CONTENT)
@atomic()
async def remove(
    id: UUID4
) -> None:
    event = await EventsDAO.get(id=id)
    return await event.delete()


@router.put("/{id:uuid}/")
@atomic()
async def update(
    id: UUID4,
    schema: EventInputDTO,
) -> EventOutputDTO:
    event = await EventsDAO.get(id=id)
    event.update_from_dict(schema.model_dump())
    await event.save()
    return await EventOutputDTO.from_tortoise_orm(event)


__all__ = [
    "router"
]
