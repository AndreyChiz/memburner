from fastapi import APIRouter

from .api_v1 import api_v1_router

root_api_router = APIRouter()

root_api_router.include_router(api_v1_router)
