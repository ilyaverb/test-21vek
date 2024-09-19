from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health_check() -> None:
    """
    Check the health of a project.
    :return:
    """

__all__ = [
    "health_check",
    "router"
]
