import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.openapi.utils import get_openapi, 

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
    #     servers=[
    #     {
    #         "url": "http://localhost:8000",
    #         "description": "Local development server"
    #     }
    # ]
  
)
main_app.include_router(
    root_api_router,
    
    
    prefix=settings.api.prefix,
)
def custom_openapi():
    if main_app.openapi_schema:
        return main_app.openapi_schema
    openapi_schema = get_openapi(
        title="Your API Title",
        version="1.0.0",
        description="Your API description",
        routes=main_app.routes,
    )
    openapi_schema["openapi"] = "3.0.0"  # Установка версии OpenAPI 3.1.0
    main_app.openapi_schema = openapi_schema
    return main_app.openapi_schema

# Назначение кастомной функции для генерации схемы OpenAPI
main_app.openapi = custom_openapi





if __name__ == "__main__":
    
    uvicorn.run(
        "main:main_app", host=settings.run.host, port=settings.run.port, reload=True
    )
