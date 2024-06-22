"""Create the FastAPI application"""

from fastapi import FastAPI

from taskmanager.application.api.controllers.main import setup_controllers


def create_app() -> FastAPI:
    """Initialize the FastAPI application and return it"""
    app = FastAPI(
        title="Task Manager",
    )

    setup_controllers(app)

    return app
