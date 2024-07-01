"""Define default router"""

from fastapi import APIRouter

default_router = APIRouter(
    prefix="",
    tags=["default"],
)


@default_router.get("/")
async def root() -> dict[str, str]:
    """Say hello endpoint"""
    return {"message": "Hello World"}
