"""Define setup_controllers function"""

from fastapi import FastAPI

from src.application.api.controllers.routers.default import default_router


def setup_controllers(app: FastAPI) -> None:
    """Configure controllers for FastAPI application"""
    app.include_router(default_router)
