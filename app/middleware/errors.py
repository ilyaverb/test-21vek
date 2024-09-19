import typing as t
from logging import getLogger

from fastapi import FastAPI
from fastapi.requests import HTTPConnection
from fastapi.responses import JSONResponse
from asyncpg.exceptions import RaiseError
from pydantic import error_wrappers
from tortoise.exceptions import (
    FieldError,
    DoesNotExist,
    IntegrityError,
    IncompleteInstanceError,
    TransactionManagementError,
)
from fastapi.exceptions import RequestValidationError
from pydantic.error_wrappers import ValidationError as PydanticValidationError
import operator
from functools import reduce

logger = getLogger(__name__)

HANDLE_EXCEPTIONS_CLASESS = (
    error_wrappers.ValidationError,
    RaiseError,
    FieldError,
    DoesNotExist,
    IntegrityError,
    IncompleteInstanceError,
    TransactionManagementError,
    RequestValidationError,
    PydanticValidationError,
)


async def process_exception(
    request: HTTPConnection,
    err_detail: str | dict,
    status_code: int,
) -> JSONResponse:
    return JSONResponse(
        {"request": str(request.url), "scope": request.scope["type"], "detail": err_detail, "status": False},
        status_code=status_code,
    )

async def handle_common_exception(request: HTTPConnection, exc: Exception) -> JSONResponse:
    logger.exception(exc)
    err_detail = str(exc)
    status_code = 400

    if isinstance(exc, PydanticValidationError) or isinstance(exc, RequestValidationError):
        status_code = 422
        err_detail = exc.errors()

    elif (
        not isinstance(exc, reduce(operator.or_, HANDLE_EXCEPTIONS_CLASESS))
    ):
        err_detail = "Internal Server Error"
        status_code = 500

    return await process_exception(
        request=request,
        err_detail=err_detail,
        status_code=status_code,
    )


async def catch_exc_middleware(request: HTTPConnection, call_next: t.Any) -> t.Any:
    try:
        return await call_next(request)
    except Exception as e:
        return await handle_common_exception(request, e)


def set_errors(app: FastAPI) -> None:
    app.middleware("http")(catch_exc_middleware)
