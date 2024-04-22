"""Initialize and run the API application"""

import asyncio

import uvicorn
from fastapi import FastAPI

from taskmanager.application.api.controllers.main import setup_controllers


def init_api(
    debug: bool = __debug__,
) -> FastAPI:
    """Initialize the FastAPI application and return it"""
    app = FastAPI(
        title="Task Manager",
        debug=debug,
    )

    setup_controllers(app)

    return app


async def run_api(app: FastAPI) -> None:
    """Run the FastAPI application"""
    config = uvicorn.Config(
        app,
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
    server = uvicorn.Server(config)
    await server.serve()


async def main() -> None:
    """Initialize the FastAPI application and run it"""
    app = init_api()
    await run_api(app)


if __name__ == "__main__":
    asyncio.run(main())
