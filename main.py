"""
Entry point for the application
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root() -> dict[str, str]:
    """Say hello endpoint"""
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str) -> dict[str, str]:
    """Say hello endpoint"""
    return {"message": f"Hello {name}"}
