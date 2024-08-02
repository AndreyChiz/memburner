import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.openapi.utils import get_openapi

from api import root_api_router

from config import settings
from core.database import db_master

from core.database.models import Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await db_master.dispose()


main_app = FastAPI(
    lifespan=lifespan,
)
main_app.include_router(
    root_api_router,
    prefix=settings.api.prefix,
)


def custom_openapi():
    if main_app.openapi_schema:
        return main_app.openapi_schema
    openapi_schema = get_openapi(
        title=settings.api.v1.openapi.title,
        version=settings.api.v1.openapi.doc_version,
        description=settings.api.v1.openapi.description,
        routes=main_app.routes,
    )
    openapi_schema["openapi"] = settings.api.v1.openapi.version
    main_app.openapi_schema = openapi_schema
    return main_app.openapi_schema


main_app.openapi = custom_openapi


if __name__ == "__main__":

    uvicorn.run(
        "main:main_app", host=settings.run.host, port=settings.run.port, reload=True
    )
