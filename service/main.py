import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

from api import root_api_router

from config import settings
from core.models import db_helper

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    db_helper.dispose()


main_app = FastAPI()
main_app.include_router(
    root_api_router,
    prefix=settings.api.prefix,
)

if __name__ == "__main__":
    uvicorn.run(
        "main:main_app", host=settings.run.host, port=settings.run.port, reload=True
    )
