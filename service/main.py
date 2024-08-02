import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

from api import frst_api_router

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
    frst_api_router,
    
    prefix=settings.api.prefix,
)


if __name__ == "__main__":
    
    uvicorn.run(
        "main:main_app", host=settings.run.host, port=settings.run.port, reload=True
    )
