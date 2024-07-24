import uvicorn
from fastapi import FastAPI

from api import root_api_router

main_app = FastAPI()
main_app.include_router(root_api_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("main:main_app", reload=True)
